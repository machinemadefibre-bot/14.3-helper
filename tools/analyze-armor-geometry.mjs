import fs from 'node:fs';
import path from 'node:path';

const filePaths = process.argv.slice(2);
if (!filePaths.length) {
  throw new Error('Usage: node tools/analyze-armor-geometry.mjs <geometry-file> [...]');
}

function readI64(buffer, offset) {
  return Number(buffer.readBigInt64LE(offset));
}

function resolveRelPtr(base, relPtr) {
  return base + relPtr;
}

function parseArmorModel(buffer, structBase) {
  const dataRelPtr = readI64(buffer, structBase);
  const sizeInBytes = buffer.readUInt32LE(structBase + 24);
  const dataStart = structBase + 0x20;
  const dataEnd = resolveRelPtr(structBase, dataRelPtr) + sizeInBytes;
  return parseArmorData(buffer.subarray(dataStart, dataEnd));
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
      bounds.count++;
      for (let vertexIndex = 0; vertexIndex < 3; vertexIndex++) {
        const vertexOffset = (pos + tri * 3 + vertexIndex) * entrySize;
        includePoint(bounds, [
          data.readFloatLE(vertexOffset),
          data.readFloatLE(vertexOffset + 4),
          data.readFloatLE(vertexOffset + 8),
        ]);
      }
    }
    groups.set(key, bounds);
    pos += vertexCount;
  }
  return groups;
}

function mergeGroups(target, source) {
  for (const [key, sourceBounds] of source) {
    const bounds = target.get(key) || newBounds();
    bounds.count += sourceBounds.count;
    includePoint(bounds, sourceBounds.min);
    includePoint(bounds, sourceBounds.max);
    target.set(key, bounds);
  }
}

function parseGeometry(filePath) {
  const buffer = fs.readFileSync(filePath);
  const armorModelCount = buffer.readUInt32LE(20);
  const armorModelsPtr = readI64(buffer, 64);
  const armorModelsOffset = resolveRelPtr(0, armorModelsPtr);
  const groups = new Map();
  for (let i = 0; i < armorModelCount; i++) {
    const modelGroups = parseArmorModel(buffer, armorModelsOffset + i * 0x20);
    mergeGroups(groups, modelGroups);
  }
  return groups;
}

for (const filePath of filePaths) {
  console.log(`GEOMETRY ${path.basename(filePath)}`);
  const groups = [...parseGeometry(filePath)]
    .map(([key, bounds]) => {
      const [materialId, layerIndex] = key.split(':').map(Number);
      return { materialId, layerIndex, ...bounds };
    })
    .sort((left, right) => (
      left.materialId - right.materialId ||
      left.layerIndex - right.layerIndex
    ));
  for (const group of groups) {
    console.log(
      `  mat ${String(group.materialId).padStart(3)} layer ${String(group.layerIndex).padStart(2)} ` +
      `tris=${String(group.count).padStart(4)} ` +
      `x=[${group.min[0].toFixed(2)},${group.max[0].toFixed(2)}] ` +
      `y=[${group.min[1].toFixed(2)},${group.max[1].toFixed(2)}] ` +
      `z=[${group.min[2].toFixed(2)},${group.max[2].toFixed(2)}]`,
    );
  }
}
