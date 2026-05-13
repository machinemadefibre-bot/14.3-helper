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

function jsonDepthDelta(text) {
  let delta = 0;
  let inString = false;
  let escape = false;
  for (const ch of text) {
    if (escape) { escape = false; continue; }
    if (ch === '\\') { if (inString) escape = true; continue; }
    if (ch === '"') { inString = !inString; continue; }
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
  const escaped = key.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  for (const line of lines) {
    if (!capturing) {
      if (line.match(new RegExp(`^  "${escaped}": \\{`))) {
        capturing = true;
      } else {
        continue;
      }
    }
    out.push(line);
    depth += jsonDepthDelta(line);
    if (depth === 0) return JSON.parse(`{${out.join('\n').replace(/,\s*$/, '')}}`)[key];
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
    total: { count: 0, area: 0, min: [Infinity, Infinity, Infinity], max: [-Infinity, -Infinity, -Infinity] },
    side: { count: 0, area: 0, min: [Infinity, Infinity, Infinity], max: [-Infinity, -Infinity, -Infinity] },
    trans: { count: 0, area: 0, min: [Infinity, Infinity, Infinity], max: [-Infinity, -Infinity, -Infinity] },
    horiz: { count: 0, area: 0, min: [Infinity, Infinity, Infinity], max: [-Infinity, -Infinity, -Infinity] },
  };
}

function triangleMetrics(vertices) {
  const [a, b, c] = vertices;
  const ab = [b[0] - a[0], b[1] - a[1], b[2] - a[2]];
  const ac = [c[0] - a[0], c[1] - a[1], c[2] - a[2]];
  const normal = [
    ab[1] * ac[2] - ab[2] * ac[1],
    ab[2] * ac[0] - ab[0] * ac[2],
    ab[0] * ac[1] - ab[1] * ac[0],
  ];
  const crossLength = Math.hypot(normal[0], normal[1], normal[2]);
  const length = crossLength || 1;
  return {
    area: crossLength / 2,
    nx: Math.abs(normal[0]) / length,
    ny: Math.abs(normal[1]) / length,
    nz: Math.abs(normal[2]) / length,
  };
}

function addTriangle(target, vertices, area) {
  target.count++;
  target.area += area;
  for (const vertex of vertices) includePoint(target, vertex);
}

function mergeTarget(target, source) {
  target.count += source.count;
  target.area += source.area;
  if (source.count) {
    includePoint(target, source.min);
    includePoint(target, source.max);
  }
}

function mergeBounds(target, source) {
  for (const key of ['total', 'side', 'trans', 'horiz']) mergeTarget(target[key], source[key]);
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
      const metrics = triangleMetrics(vertices);
      addTriangle(bounds.total, vertices, metrics.area);
      if (metrics.nx >= 0.70) addTriangle(bounds.side, vertices, metrics.area);
      if (metrics.nz >= 0.70) addTriangle(bounds.trans, vertices, metrics.area);
      if (metrics.ny >= 0.85) addTriangle(bounds.horiz, vertices, metrics.area);
    }
    groups.set(key, bounds);
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

const [geometryPath, gameParamsPath, shipKey] = process.argv.slice(2);
if (!geometryPath || !gameParamsPath || !shipKey) {
  throw new Error('Usage: node tools/inspect-geometry-side-candidates.mjs <geometry> <game-params-json> <ship-key>');
}

const materialNames = loadMaterialNames();
const ship = captureEntry(fs.readFileSync(gameParamsPath, 'utf8').replace(/^\uFEFF/, ''), shipKey);
if (!ship) throw new Error(`Unknown ship key: ${shipKey}`);
const hull = collectHullObjects(ship).at(-1);
const groups = parseGeometry(geometryPath);
const rows = [];
for (const [rawKey, thickness] of Object.entries(hull.armor || {})) {
  const encoded = Number(rawKey);
  const materialId = encoded % 65536;
  const layerIndex = Math.floor(encoded / 65536);
  const materialName = materialNames[materialId] || `unknown_${materialId}`;
  if (!/Side|Belt|Constr|Cas|SSC|SS_|Deck/.test(materialName)) continue;
  if (/Deck|Bottom/.test(materialName)) continue;
  const bounds = groups.get(`${materialId}:${layerIndex}`);
  if (!bounds) continue;
  const b = bounds.side.count ? bounds.side : bounds.total;
  const width = b.max[0] - b.min[0];
  const height = b.max[1] - b.min[1];
  const length = b.max[2] - b.min[2];
  rows.push({
    materialId,
    layerIndex,
    materialName,
    thickness,
    sideArea: bounds.side.area,
    transArea: bounds.trans.area,
    totalArea: bounds.total.area,
    sideCount: bounds.side.count,
    transCount: bounds.trans.count,
    width,
    height,
    length,
    min: b.min,
    max: b.max,
  });
}

rows.sort((a, b) => b.sideArea - a.sideArea || b.length - a.length || a.materialId - b.materialId || a.layerIndex - b.layerIndex);
for (const row of rows) {
  console.log(
    `mat=${row.materialId} layer=${row.layerIndex} ${row.materialName} ${row.thickness}mm ` +
    `sideArea=${row.sideArea.toFixed(3)} transArea=${row.transArea.toFixed(3)} totalArea=${row.totalArea.toFixed(3)} ` +
    `tris=${row.sideCount}/${row.transCount} ` +
    `x=[${row.min[0].toFixed(2)},${row.max[0].toFixed(2)}] y=[${row.min[1].toFixed(2)},${row.max[1].toFixed(2)}] z=[${row.min[2].toFixed(2)},${row.max[2].toFixed(2)}]`,
  );
}
