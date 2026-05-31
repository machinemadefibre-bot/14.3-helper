import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  mainBeltVerdict,
  normalizeApShell,
  trajectoryArmorEffectiveMm,
  usnRawPenetrationMm,
  verticalObliquityToSlopeRangeDeg,
} from './ap-penetration.mjs';

const projectRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const defaultDbPath = path.join(projectRoot, 'src', 'res_mods', 'PnFMods', 'APOvermatchAssistant', 'data', 'armor_overmatch.json');

function parseArgs(argv) {
  const result = {};
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg.startsWith('--')) {
      const key = arg.slice(2);
      const next = argv[i + 1];
      if (!next || next.startsWith('--')) result[key] = true;
      else result[key] = argv[++i];
    }
  }
  return result;
}

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8').replace(/^\uFEFF/, ''));
}

function findShip(db, query) {
  const needle = String(query || '').toLowerCase();
  for (const [key, ship] of Object.entries(db.ships || {})) {
    const aliases = [key, ship.name, ...(ship.aliases || [])].map((value) => String(value || '').toLowerCase());
    if (aliases.some((alias) => alias === needle || alias.includes(needle))) return ship;
  }
  return null;
}

function printShipTable(ship) {
  if (!ship?.mainGunAp?.table?.length) {
    throw new Error(`Ship has no AP table: ${ship?.name || 'unknown'}`);
  }
  console.log(`${ship.name} | AP shell ${ship.mainGunAp.shellName || '?'}`);
  console.log('range_km vertical_mm horizontal_mm impact_deg flight_s velocity_mps');
  for (const row of ship.mainGunAp.table) {
    console.log([
      row.rangeKm,
      row.verticalPenetrationMm,
      row.horizontalPenetrationMm,
      row.impactAngleDeg,
      row.flightTimeSec,
      row.velocityMps,
    ].join(' '));
  }
}

function runSelfTest() {
  const baltimore = normalizeApShell({
    shellName: 'PAPA001_Shell_203mm_AP_AP_Mk_19',
    caliberM: 0.203,
    massKg: 118,
    muzzleVelocityMps: 853,
    krupp: 2846,
    airDrag: 0.321,
    ricochetAtDeg: 60,
    alwaysRicochetAtDeg: 67.5,
    normalizationDeg: 7,
    hasCap: true,
  });

  assert.ok(baltimore);
  assert.equal(Math.round(usnRawPenetrationMm(baltimore)), 467);
  assert.equal(baltimore.table.length, 7);
  assert.equal(baltimore.table[0].rangeKm, 0);
  assert.equal(baltimore.table[3].rangeKm, 15);
  assert.ok(Math.abs(baltimore.table[3].verticalPenetrationMm - 274.6) < 0.8);
  assert.ok(Math.abs(baltimore.table[3].impactAngleDeg - 10.0) < 0.8);
  assert.ok(Math.abs(trajectoryArmorEffectiveMm(400, 30, 10) - 469) < 2);
  assert.deepEqual(verticalObliquityToSlopeRangeDeg(12, 8, 16), { min: 0, max: 4 });
  assert.equal(mainBeltVerdict(baltimore, { beltMm: 200, rangeKm: 10, obliquityDeg: 10, slopeDeg: 0 }), 'yes');
  assert.equal(mainBeltVerdict(baltimore, { beltMm: 200, rangeKm: 15, obliquityDeg: 75, slopeDeg: 0 }), 'no');
  assert.equal(mainBeltVerdict(null, { beltMm: 200, rangeKm: 10, obliquityDeg: 10, slopeDeg: 0 }), 'unknown');

  console.log('AP penetration diagnostics self-test passed.');
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args['self-test']) {
    runSelfTest();
    return;
  }

  const db = readJson(args.db || defaultDbPath);
  const ship = findShip(db, args.ship || 'Yamato');
  if (!ship) throw new Error(`Ship not found: ${args.ship || 'Yamato'}`);
  printShipTable(ship);
}

main();
