import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const projectRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

function loadMaterialNames() {
  const psPath = path.join(projectRoot, 'tools', 'generate-armor-db.ps1');
  const text = fs.readFileSync(psPath, 'utf8');
  const match = text.match(/\$CollisionMaterialNames = @\(([\s\S]*?)\)\r?\n\r?\nfunction Get-LatestBuildDir/);
  if (!match) throw new Error('Unable to read CollisionMaterialNames from generate-armor-db.ps1');
  return [...match[1].matchAll(/"([^"]*)"/g)].map((item) => item[1]);
}

function readI64(buffer, offset) {
  return Number(buffer.readBigInt64LE(offset));
}

function includePoint(bounds, vertex) {
  for (let i = 0; i < 3; i++) {
    bounds.min[i] = Math.min(bounds.min[i], vertex[i]);
    bounds.max[i] = Math.max(bounds.max[i], vertex[i]);
  }
}

function newBounds() {
  return {
    count: 0,
    min: [Number.POSITIVE_INFINITY, Number.POSITIVE_INFINITY, Number.POSITIVE_INFINITY],
    max: [Number.NEGATIVE_INFINITY, Number.NEGATIVE_INFINITY, Number.NEGATIVE_INFINITY],
  };
}

function horizontalNormalScore(vertices) {
  const [a, b, c] = vertices;
  const ab = [b[0] - a[0], b[1] - a[1], b[2] - a[2]];
  const ac = [c[0] - a[0], c[1] - a[1], c[2] - a[2]];
  const normal = [
    ab[1] * ac[2] - ab[2] * ac[1],
    ab[2] * ac[0] - ab[0] * ac[2],
    ab[0] * ac[1] - ab[1] * ac[0],
  ];
  const length = Math.hypot(normal[0], normal[1], normal[2]);
  return length > 0 ? Math.abs(normal[1]) / length : 0;
}

function mergeBounds(target, source) {
  target.count += source.count;
  includePoint(target, source.min);
  includePoint(target, source.max);
}

function parseArmorData(data) {
  const entrySize = 16;
  const entryCount = Math.floor(data.length / entrySize);
  const groups = new Map();
  let pos = 2;
  while (pos < entryCount) {
    if (pos + 1 >= entryCount) break;
    const nodeOffset = pos * entrySize;
    const materialId = data[nodeOffset];
    const layerIndex = data[nodeOffset + 2];
    const vertexCount = data.readUInt32LE((pos + 1) * entrySize + 12);
    pos += 2;
    if (!vertexCount) continue;
    if (pos + vertexCount > entryCount) break;
    const triCount = Math.floor(vertexCount / 3);
    const key = `${materialId}:${layerIndex}`;
    const bounds = groups.get(key) || newBounds();
    for (let tri = 0; tri < triCount; tri++) {
      const vertices = [];
      for (let vertexIndex = 0; vertexIndex < 3; vertexIndex++) {
        const vertexOffset = (pos + tri * 3 + vertexIndex) * entrySize;
        vertices.push([
          data.readFloatLE(vertexOffset),
          data.readFloatLE(vertexOffset + 4),
          data.readFloatLE(vertexOffset + 8),
        ]);
      }
      if (horizontalNormalScore(vertices) >= 0.85) {
        bounds.count++;
        for (const vertex of vertices) includePoint(bounds, vertex);
      }
    }
    if (bounds.count) groups.set(key, bounds);
    pos += vertexCount;
  }
  return groups;
}

function parseGeometry(filePath) {
  const buffer = fs.readFileSync(filePath);
  const armorModelCount = buffer.readUInt32LE(20);
  const armorModelsOffset = readI64(buffer, 64);
  const groups = new Map();
  for (let index = 0; index < armorModelCount; index++) {
    const structBase = armorModelsOffset + index * 0x20;
    const dataRelPtr = readI64(buffer, structBase);
    const sizeInBytes = buffer.readUInt32LE(structBase + 24);
    const dataStart = structBase + 0x20;
    const dataEnd = structBase + dataRelPtr + sizeInBytes;
    for (const [key, source] of parseArmorData(buffer.subarray(dataStart, dataEnd))) {
      const bounds = groups.get(key) || newBounds();
      mergeBounds(bounds, source);
      groups.set(key, bounds);
    }
  }
  return groups;
}

function jsonDepthDelta(text) {
  let delta = 0;
  let inString = false;
  let escape = false;
  for (const ch of text) {
    if (escape) {
      escape = false;
      continue;
    }
    if (ch === '\\') {
      if (inString) escape = true;
      continue;
    }
    if (ch === '"') {
      inString = !inString;
      continue;
    }
    if (inString) continue;
    if (ch === '{' || ch === '[') delta++;
    else if (ch === '}' || ch === ']') delta--;
  }
  return delta;
}

function captureEntry(text, key) {
  const lines = text.split(/\r?\n/);
  let capturing = false;
  let depth = 0;
  const out = [];
  for (const line of lines) {
    if (!capturing) {
      if (line.match(new RegExp(`^  "${key.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}": \\{`))) {
        capturing = true;
        depth = 0;
      } else {
        continue;
      }
    }
    out.push(line);
    depth += jsonDepthDelta(line);
    if (capturing && depth === 0) {
      return JSON.parse(`{${out.join('\n').replace(/,\s*$/, '')}}`)[key];
    }
  }
  return null;
}

function collectHullObjects(value, out = []) {
  if (!value || typeof value !== 'object') return out;
  for (const [key, child] of Object.entries(value)) {
    if (child && typeof child === 'object') {
      if (/Hull/.test(key) && child.armor && child.model) out.push(child);
      collectHullObjects(child, out);
    }
  }
  return out;
}

const [geometryPath, gameParamsPath, shipKey] = process.argv.slice(2);
if (!geometryPath || !gameParamsPath || !shipKey) {
  throw new Error('Usage: node tools/inspect-geometry-deck-candidates.mjs <geometry> <game-params-json> <ship-key>');
}

const materialNames = loadMaterialNames();
const groups = parseGeometry(geometryPath);
const gameParams = fs.readFileSync(gameParamsPath, 'utf8').replace(/^\uFEFF/, '');
const ship = captureEntry(gameParams, shipKey);
if (!ship) throw new Error(`Unknown ship key: ${shipKey}`);
const hull = collectHullObjects(ship).at(-1);
if (!hull) throw new Error(`No hull armor found for ship key: ${shipKey}`);

const rows = [];
for (const [rawKey, thickness] of Object.entries(hull.armor || {})) {
  const encoded = Number(rawKey);
  const materialId = encoded % 65536;
  const layerIndex = Math.floor(encoded / 65536);
  const materialName = materialNames[materialId] || `unknown_${materialId}`;
  if (!/Deck|Fdck|Hang/.test(materialName)) continue;
  if (/Cit|OCit|Tur|Art|Bridge|Funnel|Kdp|Bottom|Trans|Inclin|SideSS/.test(materialName)) continue;
  const bounds = groups.get(`${materialId}:${layerIndex}`);
  if (!bounds) continue;
  rows.push({
    materialId,
    layerIndex,
    materialName,
    thickness,
    count: bounds.count,
    min: bounds.min,
    max: bounds.max,
  });
}

rows.sort((left, right) => right.max[1] - left.max[1] || left.materialId - right.materialId || left.layerIndex - right.layerIndex);
for (const row of rows) {
  console.log(
    `mat=${row.materialId} layer=${row.layerIndex} ${row.materialName} ${row.thickness}mm ` +
    `tris=${row.count} y=[${row.min[1].toFixed(3)},${row.max[1].toFixed(3)}] ` +
    `x=[${row.min[0].toFixed(2)},${row.max[0].toFixed(2)}] z=[${row.min[2].toFixed(2)},${row.max[2].toFixed(2)}]`,
  );
}
