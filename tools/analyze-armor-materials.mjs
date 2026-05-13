import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const projectRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const gameParamsPath = process.argv[2] || 'C:\\tmp\\GameParams_ASIA.json';
const shipKeys = process.argv.slice(3);

function loadMaterialNames() {
  const psPath = path.join(projectRoot, 'tools', 'generate-armor-db.ps1');
  const text = fs.readFileSync(psPath, 'utf8');
  const match = text.match(/\$CollisionMaterialNames = @\(([\s\S]*?)\)\r?\n\r?\nfunction Get-LatestBuildDir/);
  if (!match) throw new Error('Unable to read CollisionMaterialNames from generate-armor-db.ps1');
  return [...match[1].matchAll(/"([^"]*)"/g)].map((item) => item[1]);
}

function jsonDepthDelta(line) {
  let delta = 0;
  let inString = false;
  let escape = false;
  for (const ch of line) {
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
  const startMatch = text.match(new RegExp(`^  "${key.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}": \\{`, 'm'));
  if (!startMatch) return null;
  const start = startMatch.index;
  let depth = 0;
  let inString = false;
  let escape = false;
  for (let index = start; index < text.length; index++) {
    const ch = text[index];
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
    if (ch === '{') depth++;
    else if (ch === '}') {
      depth--;
      if (depth === 0) {
        return JSON.parse(`{${text.slice(start, index + 1)}}`)[key];
      }
    }
  }
  throw new Error(`Unclosed GameParams entry: ${key}`);
}

function collectArmorObjects(value, pathParts = [], out = []) {
  if (!value || typeof value !== 'object') return out;
  if (value.armor && typeof value.armor === 'object') {
    out.push({
      path: pathParts.join('/'),
      model: value.model || '',
      armor: value.armor,
    });
  }
  for (const [key, child] of Object.entries(value)) {
    if (child && typeof child === 'object') collectArmorObjects(child, pathParts.concat(key), out);
  }
  return out;
}

function formatArmorEntry(rawKey, thickness, materialNames) {
  const encoded = Number(rawKey);
  const modelIndex = Math.floor(encoded / 65536);
  const materialId = encoded % 65536;
  const materialName = materialNames[materialId] || `unknown_${materialId}`;
  return {
    modelIndex,
    materialId,
    materialName,
    thickness: Number(thickness),
  };
}

function summarizeArmor(armor, materialNames) {
  return Object.entries(armor)
    .map(([rawKey, thickness]) => formatArmorEntry(rawKey, thickness, materialNames))
    .filter((item) => (
      /ConstrSide|Side|Belt|Cas|Cit|Deck|Fdck/.test(item.materialName) &&
      !/Tur|Art|Bridge|Funnel|Kdp|Rudder/.test(item.materialName)
    ))
    .sort((left, right) => (
      left.materialId - right.materialId ||
      left.modelIndex - right.modelIndex ||
      left.thickness - right.thickness
    ));
}

const materialNames = loadMaterialNames();
const text = fs.readFileSync(gameParamsPath, 'utf8').replace(/^\uFEFF/, '');
for (const key of shipKeys) {
  const entry = captureEntry(text, key);
  if (!entry) {
    console.log(`SHIP ${key}: not found`);
    continue;
  }
  console.log(`SHIP ${key}`);
  const armorObjects = collectArmorObjects(entry)
    .filter((item) => /Hull/.test(item.path))
    .slice(0, 8);
  for (const item of armorObjects) {
    console.log(`  ${item.path} model=${item.model || '-'}`);
    for (const armorEntry of summarizeArmor(item.armor, materialNames)) {
      const indexText = `mi${armorEntry.modelIndex}`;
      console.log(
        `    ${indexText.padEnd(5)} mat ${String(armorEntry.materialId).padStart(3)} ` +
        `${armorEntry.materialName.padEnd(24)} ${armorEntry.thickness} mm`,
      );
    }
  }
}
