#!/usr/bin/env node
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';

const KNOTS_PER_MPS = 1.9438444924406;
const RAD_TO_DEG = 180 / Math.PI;

function usage() {
  console.log(`Usage:
  node tools/analyze-replay-heel.mjs --replay <file.wowsreplay> [--game-dir <WoWS dir>] [--replayshark <replayshark.exe>] [--out-csv <file.csv>]
  node tools/analyze-replay-heel.mjs --meta <meta.json> --packets <packets.bin> [--out-csv <file.csv>]

Options:
  --all-entities          Analyze every entity with position samples instead of only own ship.
  --game-dir <path>       Decode ruddersAngle/serverSpeedRaw with replayshark game specs.
  --min-speed-knots <n>   Ignore samples below this speed. Default: 1.
  --max-dt <seconds>      Ignore position gaps above this interval. Default: 5.
  --max-speed-knots <n>   Ignore samples above this speed. Default: 80.
  --max-turn-deg-sec <n>  Ignore turn-rate spikes above this value. Default: 30.
  --sample-hz <n>         Resample motion at a fixed rate before differencing. Default: 7.
  --speed-bin <knots>     Speed bucket size. Default: 5.
  --turn-bin <deg/s>      Turn-rate bucket size. Default: 1.
  --top <n>               Print top per-entity summaries. Default: 12.

Notes:
  Without decoded entity_defs, real rudder percentage is unavailable. The report
  uses abs yaw-rate and turnRatePctOfReplayMax as a temporary rudder proxy.`);
}

function parseArgs(argv) {
  const args = {
    allEntities: false,
    maxDt: 5,
    maxSpeedKnots: 80,
    maxTurnDegSec: 30,
    minSpeedKnots: 1,
    sampleHz: 7,
    speedBin: 5,
    turnBin: 1,
    top: 12,
  };
  for (let i = 2; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === '--help' || arg === '-h') {
      args.help = true;
    } else if (arg === '--all-entities') {
      args.allEntities = true;
    } else if (arg === '--replay') {
      args.replay = argv[++i];
    } else if (arg === '--replayshark') {
      args.replayshark = argv[++i];
    } else if (arg === '--game-dir') {
      args.gameDir = argv[++i];
    } else if (arg === '--meta') {
      args.meta = argv[++i];
    } else if (arg === '--packets') {
      args.packets = argv[++i];
    } else if (arg === '--out-csv') {
      args.outCsv = argv[++i];
    } else if (arg === '--max-dt') {
      args.maxDt = Number(argv[++i]);
    } else if (arg === '--max-speed-knots') {
      args.maxSpeedKnots = Number(argv[++i]);
    } else if (arg === '--max-turn-deg-sec') {
      args.maxTurnDegSec = Number(argv[++i]);
    } else if (arg === '--sample-hz') {
      args.sampleHz = Number(argv[++i]);
    } else if (arg === '--min-speed-knots') {
      args.minSpeedKnots = Number(argv[++i]);
    } else if (arg === '--speed-bin') {
      args.speedBin = Number(argv[++i]);
    } else if (arg === '--turn-bin') {
      args.turnBin = Number(argv[++i]);
    } else if (arg === '--top') {
      args.top = Number(argv[++i]);
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }
  return args;
}

function findDefaultReplayShark() {
  const checkoutRoot = path.join(
    process.cwd(),
    'tools',
    'rust',
    'cargo',
    'git',
    'checkouts',
    'wows-toolkit-34d7c18c7314dd0f',
    '868c346',
  );
  const candidate = path.join(checkoutRoot, 'target', 'debug', 'replayshark.exe');
  if (fs.existsSync(candidate)) return candidate;
  return 'replayshark.exe';
}

function sanitizeName(filePath) {
  return path.basename(filePath).replace(/[^A-Za-z0-9_.-]+/g, '_').replace(/\.wowsreplay$/i, '');
}

function decryptReplay(replayPath, replaysharkPath) {
  const outDir = path.join(process.cwd(), 'build', 'scratch', 'replay-heel');
  fs.mkdirSync(outDir, { recursive: true });
  const stem = sanitizeName(replayPath);
  const meta = path.join(outDir, `${stem}.meta.json`);
  const packets = path.join(outDir, `${stem}.packets.bin`);
  const result = spawnSync(
    replaysharkPath,
    ['decrypt', '--meta-output', meta, '--packets-output', packets, replayPath],
    { stdio: 'inherit' },
  );
  if (result.status !== 0) {
    throw new Error(`replayshark decrypt failed with exit code ${result.status}`);
  }
  return { meta, packets };
}

function readReplayInputs(args) {
  if (args.replay) {
    return {
      ...decryptReplay(path.resolve(args.replay), path.resolve(args.replayshark || findDefaultReplayShark())),
      replay: path.resolve(args.replay),
      replayshark: path.resolve(args.replayshark || findDefaultReplayShark()),
    };
  }
  if (!args.meta || !args.packets) {
    throw new Error('Provide either --replay or both --meta and --packets.');
  }
  return { meta: args.meta, packets: args.packets };
}

function decodeEntityProperties(replayPath, replaysharkPath, gameDir) {
  if (!replayPath || !gameDir) return new Map();
  const result = spawnSync(
    replaysharkPath,
    ['-g', path.resolve(gameDir), 'investigate', '--filter-packet', '0x07', replayPath],
    { encoding: 'utf8', maxBuffer: 256 * 1024 * 1024 },
  );
  if (result.status !== 0) {
    throw new Error(`replayshark property decode failed with exit code ${result.status}: ${result.stderr}`);
  }
  const wanted = new Set(['ruddersAngle', 'serverSpeedRaw', 'enginePower', 'engineDir']);
  const byEntity = new Map();
  for (const line of result.stdout.split(/\r?\n/)) {
    if (!line.trim()) continue;
    let packet;
    try {
      packet = JSON.parse(line);
    } catch {
      continue;
    }
    const prop = packet.payload?.EntityProperty;
    if (!prop || !wanted.has(prop.property)) continue;
    if (!byEntity.has(prop.entity_id)) byEntity.set(prop.entity_id, []);
    byEntity.get(prop.entity_id).push({
      clock: packet.clock,
      property: prop.property,
      value: prop.value,
    });
  }
  for (const events of byEntity.values()) {
    events.sort((a, b) => a.clock - b.clock);
  }
  return byEntity;
}

function readU32(buffer, offset) {
  return buffer.readUInt32LE(offset);
}

function readF32(buffer, offset) {
  return buffer.readFloatLE(offset);
}

function radToDeg(value) {
  return value * RAD_TO_DEG;
}

function normalizeDeg(delta) {
  while (delta > 180) delta -= 360;
  while (delta < -180) delta += 360;
  return delta;
}

function parsePackets(buffer) {
  const entities = new Map();
  const cameraSamples = [];
  let ownShipId = null;
  let totalPackets = 0;
  let positionPackets = 0;
  let orientationPackets = 0;
  let skippedPackets = 0;

  function addSample(pid, sample) {
    if (!entities.has(pid)) entities.set(pid, []);
    entities.get(pid).push(sample);
  }

  for (let offset = 0; offset + 12 <= buffer.length;) {
    const packetSize = readU32(buffer, offset);
    const packetType = readU32(buffer, offset + 4);
    const clock = readF32(buffer, offset + 8);
    const payloadOffset = offset + 12;
    const nextOffset = payloadOffset + packetSize;
    if (packetSize < 0 || nextOffset > buffer.length) {
      skippedPackets++;
      break;
    }

    totalPackets++;
    if (packetType === 0x20 && packetSize >= 4) {
      ownShipId = readU32(buffer, payloadOffset);
    } else if (packetType === 0x0a && packetSize >= 45) {
      const pid = readU32(buffer, payloadOffset);
      const x = readF32(buffer, payloadOffset + 8);
      const y = readF32(buffer, payloadOffset + 12);
      const z = readF32(buffer, payloadOffset + 16);
      const directionX = readF32(buffer, payloadOffset + 20);
      const directionY = readF32(buffer, payloadOffset + 24);
      const directionZ = readF32(buffer, payloadOffset + 28);
      const yaw = readF32(buffer, payloadOffset + 32);
      const pitch = readF32(buffer, payloadOffset + 36);
      const roll = readF32(buffer, payloadOffset + 40);
      addSample(pid, {
        clock,
        x,
        y,
        z,
        directionX,
        directionY,
        directionZ,
        yawDeg: radToDeg(yaw),
        pitchDeg: radToDeg(pitch),
        rollDeg: radToDeg(roll),
        source: 'position',
      });
      positionPackets++;
    } else if (packetType === 0x2c && packetSize >= 32) {
      const pid = readU32(buffer, payloadOffset);
      const parentId = readU32(buffer, payloadOffset + 4);
      const x = readF32(buffer, payloadOffset + 8);
      const y = readF32(buffer, payloadOffset + 12);
      const z = readF32(buffer, payloadOffset + 16);
      const yaw = readF32(buffer, payloadOffset + 20);
      const pitch = readF32(buffer, payloadOffset + 24);
      const roll = readF32(buffer, payloadOffset + 28);
      const entityId = parentId || pid;
      addSample(entityId, {
        clock,
        x,
        y,
        z,
        directionX: 0,
        directionY: 0,
        directionZ: 0,
        yawDeg: radToDeg(yaw),
        pitchDeg: radToDeg(pitch),
        rollDeg: radToDeg(roll),
        source: 'orientation',
      });
      orientationPackets++;
    } else if (packetType === 0x25 && packetSize >= 60) {
      cameraSamples.push({
        clock,
        x: readF32(buffer, payloadOffset + 36),
        y: readF32(buffer, payloadOffset + 40),
        z: readF32(buffer, payloadOffset + 44),
        directionX: readF32(buffer, payloadOffset + 48),
        directionY: readF32(buffer, payloadOffset + 52),
        directionZ: readF32(buffer, payloadOffset + 56),
      });
    }
    offset = nextOffset;
  }

  return { entities, cameraSamples, ownShipId, totalPackets, positionPackets, orientationPackets, skippedPackets };
}

function mergeOwnShipCameraTrack(track, cameraSamples) {
  if (!track?.length || !cameraSamples.length) return track || [];
  const sortedCamera = [...cameraSamples].sort((a, b) => a.clock - b.clock);
  let cameraIndex = 0;
  return [...track]
    .sort((a, b) => a.clock - b.clock)
    .map((sample) => {
      while (
        cameraIndex + 1 < sortedCamera.length &&
        Math.abs(sortedCamera[cameraIndex + 1].clock - sample.clock) <= Math.abs(sortedCamera[cameraIndex].clock - sample.clock)
      ) {
        cameraIndex++;
      }
      const camera = sortedCamera[cameraIndex];
      if (!camera || Math.abs(camera.clock - sample.clock) > 0.2) return sample;
      return {
        ...sample,
        x: camera.x,
        y: camera.y,
        z: camera.z,
        directionX: camera.directionX,
        directionY: camera.directionY,
        directionZ: camera.directionZ,
        source: `${sample.source}+camera`,
      };
    });
}

function enrichTrackWithProperties(track, propertyEvents) {
  if (!track?.length || !propertyEvents?.length) return track || [];
  const sortedEvents = [...propertyEvents].sort((a, b) => a.clock - b.clock);
  let eventIndex = 0;
  const state = {
    ruddersAngle: null,
    serverSpeedRaw: null,
    enginePower: null,
    engineDir: null,
  };
  return [...track]
    .sort((a, b) => a.clock - b.clock)
    .map((sample) => {
      while (eventIndex < sortedEvents.length && sortedEvents[eventIndex].clock <= sample.clock) {
        const event = sortedEvents[eventIndex];
        state[event.property] = event.value;
        eventIndex++;
      }
      const rudderPercent = Number.isFinite(state.ruddersAngle)
        ? Math.min(100, Math.abs(state.ruddersAngle) / (Math.PI / 6) * 100)
        : null;
      const serverSpeedKnots = Number.isFinite(state.serverSpeedRaw)
        ? Math.abs(state.serverSpeedRaw) / 5
        : null;
      return {
        ...sample,
        hasDecodedProperties: true,
        rudderPercent,
        ruddersAngleRad: state.ruddersAngle,
        serverSpeedRaw: state.serverSpeedRaw,
        serverSpeedKnots,
        enginePower: state.enginePower,
        engineDir: state.engineDir,
      };
    });
}

function quantile(sorted, q) {
  if (!sorted.length) return 0;
  const index = Math.min(sorted.length - 1, Math.max(0, (sorted.length - 1) * q));
  const lo = Math.floor(index);
  const hi = Math.ceil(index);
  if (lo === hi) return sorted[lo];
  return sorted[lo] + (sorted[hi] - sorted[lo]) * (index - lo);
}

function summarize(values) {
  const sorted = [...values].sort((a, b) => a - b);
  return {
    count: sorted.length,
    mean: sorted.reduce((sum, value) => sum + value, 0) / Math.max(1, sorted.length),
    p50: quantile(sorted, 0.5),
    p90: quantile(sorted, 0.9),
    max: sorted[sorted.length - 1] || 0,
  };
}

function bucket(value, size) {
  if (!Number.isFinite(value) || size <= 0) return 'unknown';
  const min = Math.floor(value / size) * size;
  const max = min + size;
  return `${min}-${max}`;
}

function resampleTrack(track, sampleHz) {
  if (!Number.isFinite(sampleHz) || sampleHz <= 0 || !track?.length) {
    return track || [];
  }
  const sorted = [...track].sort((a, b) => a.clock - b.clock);
  const interval = 1 / sampleHz;
  const maxNearestDelta = interval * 0.55;
  const result = [];
  let sourceIndex = 0;
  let nextClock = Math.ceil(sorted[0].clock / interval) * interval;
  const endClock = sorted[sorted.length - 1].clock;

  while (nextClock <= endClock) {
    while (
      sourceIndex + 1 < sorted.length &&
      Math.abs(sorted[sourceIndex + 1].clock - nextClock) <= Math.abs(sorted[sourceIndex].clock - nextClock)
    ) {
      sourceIndex++;
    }
    const sample = sorted[sourceIndex];
    if (sample && Math.abs(sample.clock - nextClock) <= maxNearestDelta) {
      if (!result.length || result[result.length - 1].clock !== sample.clock) {
        result.push({ ...sample, sampledClock: nextClock });
      }
    }
    nextClock += interval;
  }
  return result.length >= 2 ? result : sorted;
}

function makeSamples(track, options) {
  const samples = [];
  const sorted = resampleTrack(track, options.sampleHz);
  for (let i = 1; i < sorted.length; i++) {
    const previous = sorted[i - 1];
    const current = sorted[i];
    const currentClock = Number.isFinite(current.sampledClock) ? current.sampledClock : current.clock;
    const previousClock = Number.isFinite(previous.sampledClock) ? previous.sampledClock : previous.clock;
    const dt = currentClock - previousClock;
    if (dt <= 0 || dt > options.maxDt) continue;

    const dx = current.x - previous.x;
    const dz = current.z - previous.z;
    const distance = Math.hypot(dx, dz);
    const deltaSpeedKnots = (distance / dt) * KNOTS_PER_MPS;
    const directionSpeedKnots = Math.hypot(current.directionX, current.directionZ) * KNOTS_PER_MPS;
    let speedKnots = null;
    if (current.hasDecodedProperties) {
      if (!Number.isFinite(current.serverSpeedKnots)) continue;
      speedKnots = current.serverSpeedKnots;
    } else {
      speedKnots = (
        deltaSpeedKnots >= options.minSpeedKnots &&
        deltaSpeedKnots <= options.maxSpeedKnots
      ) ? deltaSpeedKnots : directionSpeedKnots;
    }
    if (speedKnots < options.minSpeedKnots) continue;
    if (speedKnots > options.maxSpeedKnots) continue;

    const yawDeltaDeg = normalizeDeg(current.yawDeg - previous.yawDeg);
    const turnRateDegPerSec = Math.abs(yawDeltaDeg / dt);
    if (turnRateDegPerSec > options.maxTurnDegSec) continue;
    samples.push({
      clock: current.clock,
      speedKnots,
      directionSpeedKnots,
      serverSpeedKnots: current.serverSpeedKnots,
      rudderPercent: current.rudderPercent,
      turnRateDegPerSec,
      rollDeg: current.rollDeg,
      absRollDeg: Math.abs(current.rollDeg),
      pitchDeg: current.pitchDeg,
      yawDeg: current.yawDeg,
    });
  }
  return samples;
}

function analyzeEntity(entityId, track, options) {
  const samples = makeSamples(track, options);
  const maxTurnRate = Math.max(0, ...samples.map((sample) => sample.turnRateDegPerSec));
  const buckets = new Map();
  for (const sample of samples) {
    const speedBucket = bucket(sample.speedKnots, options.speedBin);
    const turnBucket = bucket(sample.turnRateDegPerSec, options.turnBin);
    const rudderBucket = Number.isFinite(sample.rudderPercent)
      ? bucket(sample.rudderPercent, 25)
      : 'unknown';
    const key = `${speedBucket}|${turnBucket}|${rudderBucket}`;
    if (!buckets.has(key)) {
      buckets.set(key, { speedBucket, turnBucket, rudderBucket, samples: [] });
    }
    buckets.get(key).samples.push({
      ...sample,
      turnRatePctOfReplayMax: maxTurnRate > 0 ? sample.turnRateDegPerSec / maxTurnRate * 100 : 0,
    });
  }
  const absRoll = samples.map((sample) => sample.absRollDeg);
  const speeds = samples.map((sample) => sample.speedKnots);
  const turns = samples.map((sample) => sample.turnRateDegPerSec);
  return {
    entityId,
    rawSamples: track.length,
    samples,
    maxTurnRate,
    summary: {
      speed: summarize(speeds),
      absRoll: summarize(absRoll),
      turnRate: summarize(turns),
    },
    buckets: [...buckets.values()]
      .map((entry) => {
        const rolls = entry.samples.map((sample) => sample.absRollDeg);
        const speedsInBucket = entry.samples.map((sample) => sample.speedKnots);
        const turnsInBucket = entry.samples.map((sample) => sample.turnRateDegPerSec);
        const turnPct = entry.samples.map((sample) => sample.turnRatePctOfReplayMax);
        const ruddersInBucket = entry.samples
          .map((sample) => sample.rudderPercent)
          .filter(Number.isFinite);
        return {
          entityId,
          speedBucket: entry.speedBucket,
          turnBucket: entry.turnBucket,
          rudderBucket: entry.rudderBucket,
          count: entry.samples.length,
          speedMeanKnots: summarize(speedsInBucket).mean,
          turnRateMeanDegPerSec: summarize(turnsInBucket).mean,
          turnRatePctOfReplayMaxMean: summarize(turnPct).mean,
          rudderMeanPct: ruddersInBucket.length ? summarize(ruddersInBucket).mean : null,
          absRollMeanDeg: summarize(rolls).mean,
          absRollP90Deg: summarize(rolls).p90,
          absRollMaxDeg: summarize(rolls).max,
        };
      })
      .sort((a, b) => b.count - a.count),
  };
}

function format(value, digits = 2) {
  return Number.isFinite(value) ? value.toFixed(digits) : '';
}

function writeCsv(filePath, rows) {
  const header = [
    'ship',
    'entityId',
    'speedBucketKnots',
    'turnRateBucketDegPerSec',
    'rudderBucketPct',
    'count',
    'speedMeanKnots',
    'turnRateMeanDegPerSec',
    'turnRatePctOfReplayMaxMean',
    'rudderMeanPct',
    'absRollMeanDeg',
    'absRollP90Deg',
    'absRollMaxDeg',
  ];
  const lines = [header.join(',')];
  for (const row of rows) {
    lines.push([
      row.ship,
      row.entityId,
      row.speedBucket,
      row.turnBucket,
      row.rudderBucket,
      row.count,
      format(row.speedMeanKnots),
      format(row.turnRateMeanDegPerSec),
      format(row.turnRatePctOfReplayMaxMean),
      row.rudderMeanPct === null ? '' : format(row.rudderMeanPct),
      format(row.absRollMeanDeg),
      format(row.absRollP90Deg),
      format(row.absRollMaxDeg),
    ].join(','));
  }
  fs.mkdirSync(path.dirname(path.resolve(filePath)), { recursive: true });
  fs.writeFileSync(filePath, `${lines.join('\n')}\n`);
}

function main() {
  const args = parseArgs(process.argv);
  if (args.help) {
    usage();
    return;
  }
  const inputs = readReplayInputs(args);
  const meta = JSON.parse(fs.readFileSync(inputs.meta, 'utf8'));
  const packetData = fs.readFileSync(inputs.packets);
  const parsed = parsePackets(packetData);
  const propertyEvents = decodeEntityProperties(inputs.replay, inputs.replayshark || findDefaultReplayShark(), args.gameDir);
  const ship = meta.playerVehicle || 'unknown';

  const entityIds = args.allEntities
    ? [...parsed.entities.keys()]
    : [parsed.ownShipId].filter((id) => id !== null && parsed.entities.has(id));

  if (!entityIds.length) {
    throw new Error('No matching entity position samples found. Try --all-entities.');
  }

  const analyses = entityIds
    .map((id) => {
      const rawTrack = parsed.entities.get(id);
      const positionTrack = !args.allEntities && id === parsed.ownShipId
        ? mergeOwnShipCameraTrack(rawTrack, parsed.cameraSamples)
        : rawTrack;
      const track = enrichTrackWithProperties(positionTrack, propertyEvents.get(id));
      return analyzeEntity(id, track, args);
    })
    .filter((analysis) => analysis.samples.length > 0)
    .sort((a, b) => b.samples.length - a.samples.length);

  const rows = analyses.flatMap((analysis) => analysis.buckets.map((row) => ({ ...row, ship })));
  if (args.outCsv) writeCsv(args.outCsv, rows);

  console.log(`Replay: ${path.basename(args.replay || inputs.meta)}`);
  console.log(`Ship: ${ship}`);
  console.log(`Version: ${meta.clientVersionFromExe || 'unknown'}`);
  console.log(`Packets: ${parsed.totalPackets}, position packets: ${parsed.positionPackets}, orientation packets: ${parsed.orientationPackets}, entities: ${parsed.entities.size}`);
  console.log(`Own ship entity: ${parsed.ownShipId ?? 'unknown'}`);
  console.log(propertyEvents.size
    ? `Rudder: decoded EntityProperty updates for ${propertyEvents.size} entities.`
    : 'Rudder: real rudder percentage unavailable without decoded entity_defs; using turn-rate proxy.');
  console.log('');

  for (const analysis of analyses.slice(0, args.top)) {
    console.log(`Entity ${analysis.entityId}: raw=${analysis.rawSamples}, samples=${analysis.samples.length}`);
    console.log(`  speed mean/p90/max kt: ${format(analysis.summary.speed.mean)} / ${format(analysis.summary.speed.p90)} / ${format(analysis.summary.speed.max)}`);
    console.log(`  turn mean/p90/max deg/s: ${format(analysis.summary.turnRate.mean)} / ${format(analysis.summary.turnRate.p90)} / ${format(analysis.summary.turnRate.max)}`);
    console.log(`  abs roll mean/p90/max deg: ${format(analysis.summary.absRoll.mean)} / ${format(analysis.summary.absRoll.p90)} / ${format(analysis.summary.absRoll.max)}`);
    console.log('  busiest buckets:');
    for (const row of analysis.buckets.slice(0, 8)) {
      console.log(
        `    speed ${row.speedBucket} kt, turn ${row.turnBucket} deg/s, n=${row.count}: ` +
        `roll mean/p90/max ${format(row.absRollMeanDeg)}/${format(row.absRollP90Deg)}/${format(row.absRollMaxDeg)} deg, ` +
        `turnProxy ${format(row.turnRatePctOfReplayMaxMean, 1)}%`,
      );
    }
  }

  if (args.outCsv) {
    console.log('');
    console.log(`CSV: ${path.resolve(args.outCsv)}`);
  }
}

try {
  main();
} catch (error) {
  console.error(`ERROR: ${error.message}`);
  process.exit(1);
}
