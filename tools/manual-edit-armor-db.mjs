import fs from 'node:fs';
import path from 'node:path';
import readline from 'node:readline';
import { fileURLToPath } from 'node:url';

const projectRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

function parseArgs(argv) {
  const args = {};
  for (let i = 0; i < argv.length; i++) {
    const key = argv[i];
    if (!key.startsWith('--')) continue;
    const name = key.slice(2);
    const next = argv[i + 1];
    if (!next || next.startsWith('--')) {
      args[name] = true;
    } else {
      args[name] = next;
      i++;
    }
  }
  return args;
}

function readJsonFile(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8').replace(/^\uFEFF/, ''));
}

function unique(values) {
  return [...new Set((values || [])
    .map(Number)
    .filter((value) => Number.isFinite(value) && value > 0)
    .map((value) => Math.round(value * 10) / 10))]
    .sort((a, b) => a - b);
}

function formatValues(values) {
  const clean = unique(values);
  return clean.length ? clean.join('/') : '-';
}

function parseValues(input) {
  const text = String(input || '').trim();
  if (!text) return null;
  if (text === '-') return [];
  const values = text.split('/').map((item) => {
    const value = Number(item.trim());
    if (!Number.isFinite(value) || value <= 0) {
      throw new Error(`Invalid value: ${item}`);
    }
    return value;
  });
  return unique(values);
}

function parseScalar(input) {
  const text = String(input || '').trim();
  if (!text) return undefined;
  if (text === '-') return null;
  const value = Number(text);
  if (!Number.isFinite(value) || value <= 0) {
    throw new Error(`Invalid value: ${input}`);
  }
  return Math.round(value * 10) / 10;
}

function pythonLiteral(value, depth = 0) {
  const indent = '  '.repeat(depth);
  const nextIndent = '  '.repeat(depth + 1);
  if (value === null || value === undefined) return 'None';
  if (typeof value === 'boolean') return value ? 'True' : 'False';
  if (typeof value === 'number') {
    if (!Number.isFinite(value)) throw new Error(`Cannot write non-finite number: ${value}`);
    return String(value);
  }
  if (typeof value === 'string') return JSON.stringify(value);
  if (Array.isArray(value)) {
    if (!value.length) return '[]';
    const items = value.map((item) => `${nextIndent}${pythonLiteral(item, depth + 1)}`);
    return `[\n${items.join(',\n')}\n${indent}]`;
  }
  if (typeof value === 'object') {
    const entries = Object.entries(value);
    if (!entries.length) return '{}';
    const items = entries.map(([key, item]) => (
      `${nextIndent}${pythonLiteral(key)}: ${pythonLiteral(item, depth + 1)}`
    ));
    return `{\n${items.join(',\n')}\n${indent}}`;
  }
  throw new Error(`Unsupported value in Python database: ${typeof value}`);
}

function writePythonDatabase(database, outPath) {
  const pyOutPath = outPath.replace(/\.[^.]*$/, '.py');
  const pyText = `# -*- coding: utf-8 -*-\n# Generated from armor_overmatch.json. WoWS ModsAPI blocks the json module.\nDATABASE = ${pythonLiteral(database)}\n`;
  fs.writeFileSync(pyOutPath, pyText, 'utf8');
}

function writeDatabase(database, outPath) {
  fs.writeFileSync(outPath, `${JSON.stringify(database, null, 2)}\n`, 'utf8');
  writePythonDatabase(database, outPath);
}

function backupDatabase(jsonPath) {
  const snapshotDir = path.join(projectRoot, 'tools', 'armor_snapshots');
  fs.mkdirSync(snapshotDir, { recursive: true });
  const db = readJsonFile(jsonPath);
  const build = String(db.meta?.gameBuild || 'unknown-build').replace(/[^A-Za-z0-9._-]+/g, '_');
  const stamp = new Date().toISOString().replace(/[-:]/g, '').replace(/\..*$/, '').replace('T', '-');
  const base = path.join(snapshotDir, `armor_overmatch.manual.${build}.${stamp}`);
  fs.copyFileSync(jsonPath, `${base}.json`);
  const pyPath = jsonPath.replace(/\.[^.]*$/, '.py');
  if (fs.existsSync(pyPath)) fs.copyFileSync(pyPath, `${base}.py`);
  return `${base}.json`;
}

function keyParts(key) {
  const match = String(key).match(/^P(.)(S)([ABCDS])(\d{3})_/);
  if (!match) return null;
  const code = Number(match[4]);
  let tier = code % 100;
  if (tier > 11) tier %= 10;
  if (tier === 0) tier = 10;
  return {
    nation: match[1],
    type: match[3],
    tier,
  };
}

const nationNames = {
  A: 'USA',
  B: 'UK',
  F: 'France',
  G: 'Germany',
  H: 'Netherlands',
  I: 'Italy',
  J: 'Japan',
  R: 'USSR',
  S: 'Spain',
  U: 'Commonwealth',
  V: 'Pan-America',
  W: 'Europe',
  X: 'Special',
  Z: 'Pan-Asia',
};

const typeNames = {
  A: 'Carrier',
  B: 'Battleship',
  C: 'Cruiser',
  D: 'Destroyer',
  S: 'Submarine',
};

const typeChoices = ['A', 'B', 'C', 'D', 'S'];

const fieldChoices = [
  { label: 'Bow plating', kind: 'values', get: (ship) => ship.armor?.bowStern?.bow, set: (ship, values) => { ship.armor.bowStern.bow = values; } },
  { label: 'Stern plating', kind: 'values', get: (ship) => ship.armor?.bowStern?.stern, set: (ship, values) => { ship.armor.bowStern.stern = values; } },
  { label: 'Deck', kind: 'values', get: (ship) => ship.armor?.deck?.values, set: (ship, values) => { ship.armor.deck.values = values; } },
  { label: 'Side', kind: 'values', get: (ship) => ship.armor?.side?.values, set: (ship, values) => { ship.armor.side.values = values; } },
  { label: 'Bow belt', kind: 'values', get: (ship) => ship.armor?.extendedBowSternBelt?.bow, set: (ship, values) => { ship.armor.extendedBowSternBelt.bow = values; syncBelt(ship); } },
  { label: 'Stern belt', kind: 'values', get: (ship) => ship.armor?.extendedBowSternBelt?.stern, set: (ship, values) => { ship.armor.extendedBowSternBelt.stern = values; syncBelt(ship); } },
  { label: 'Main gun caliber', kind: 'scalar', get: (ship) => ship.mainGunCaliberMm, set: (ship, value) => { ship.mainGunCaliberMm = value; } },
  { label: 'HE penetration', kind: 'scalar', get: (ship) => ship.mainGunHePenMm, set: (ship, value) => { ship.mainGunHePenMm = value; } },
  { label: 'SAP penetration', kind: 'scalar', get: (ship) => ship.mainGunSapPenMm, set: (ship, value) => { ship.mainGunSapPenMm = value; } },
];

function ensureArmorShape(ship) {
  ship.armor ||= {};
  ship.armor.bowStern ||= {};
  ship.armor.bowStern.bow ||= [];
  ship.armor.bowStern.stern ||= [];
  ship.armor.deck ||= {};
  ship.armor.deck.values ||= [];
  ship.armor.side ||= {};
  ship.armor.side.values ||= [];
  ship.armor.extendedBowSternBelt ||= {};
  ship.armor.extendedBowSternBelt.values ||= [];
  ship.armor.extendedBowSternBelt.bow ||= [];
  ship.armor.extendedBowSternBelt.stern ||= [];
}

function syncBelt(ship) {
  const belt = ship.armor.extendedBowSternBelt;
  belt.bow = unique(belt.bow || []);
  belt.stern = unique(belt.stern || []);
  belt.values = unique([...(belt.bow || []), ...(belt.stern || [])]);
  belt.present = belt.values.length > 0;
}

function displayShip(shipKey, ship) {
  const parts = keyParts(shipKey);
  const nation = parts ? (nationNames[parts.nation] || parts.nation) : '?';
  const type = parts ? (typeNames[parts.type] || parts.type) : '?';
  const tier = parts ? parts.tier : '?';
  return `${shipKey} | ${ship.name || shipKey} | ${nation} | ${type} | T${tier}`;
}

function createReader() {
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  return {
    question(prompt) {
      return new Promise((resolve) => rl.question(prompt, (answer) => resolve(answer)));
    },
    close() {
      rl.close();
    },
  };
}

async function askNumber(reader, prompt, min, max, defaultValue = '') {
  while (true) {
    const suffix = defaultValue === '' ? '' : ` [${defaultValue}]`;
    const answer = (await reader.question(`${prompt}${suffix}: `)).trim();
    if (!answer && defaultValue !== '') return defaultValue;
    const value = Number(answer);
    if (Number.isInteger(value) && value >= min && value <= max) return value;
    console.log(`Enter a number from ${min} to ${max}.`);
  }
}

async function askYesNo(reader, prompt, defaultNo = true) {
  const suffix = defaultNo ? '[y/N]' : '[Y/n]';
  const answer = (await reader.question(`${prompt} ${suffix}: `)).trim().toLowerCase();
  if (!answer) return !defaultNo;
  return answer === 'y' || answer === 'yes';
}

async function pickFilters(reader, ships) {
  const nations = [...new Set(ships.map((item) => item.parts?.nation).filter(Boolean))].sort();
  console.log('');
  console.log('Country filter');
  console.log('  0. All');
  nations.forEach((code, index) => console.log(`  ${index + 1}. ${nationNames[code] || code}`));
  const nationIndex = await askNumber(reader, 'Country', 0, nations.length, 0);
  const nation = nationIndex === 0 ? '' : nations[nationIndex - 1];

  console.log('');
  console.log('Ship type');
  typeChoices.forEach((code, index) => console.log(`  ${index + 1}. ${typeNames[code]}`));
  console.log('  0. All');
  const typeIndex = await askNumber(reader, 'Type', 0, typeChoices.length, 0);
  const type = typeIndex === 0 ? '' : typeChoices[typeIndex - 1];

  const tier = await askNumber(reader, 'Tier 1-11, or 0 for all', 0, 11, 0);
  return { nation, type, tier };
}

function filterShips(ships, filters) {
  return ships.filter((item) => {
    if (!item.parts) return false;
    if (filters.nation && item.parts.nation !== filters.nation) return false;
    if (filters.type && item.parts.type !== filters.type) return false;
    if (filters.tier && item.parts.tier !== filters.tier) return false;
    return true;
  });
}

async function pickShip(reader, ships) {
  if (!ships.length) return null;
  console.log('');
  ships.slice(0, 120).forEach((item, index) => {
    console.log(`  ${index + 1}. ${displayShip(item.key, item.ship)}`);
  });
  if (ships.length > 120) {
    console.log(`  ... ${ships.length - 120} more hidden. Narrow the filters if needed.`);
  }
  const max = Math.min(ships.length, 120);
  const index = await askNumber(reader, 'Ship number', 1, max);
  return ships[index - 1];
}

async function editShip(reader, db, jsonPath, shipItem) {
  const ship = shipItem.ship;
  ensureArmorShape(ship);

  console.log('');
  console.log(displayShip(shipItem.key, ship));
  fieldChoices.forEach((field, index) => {
    const current = field.kind === 'values' ? formatValues(field.get(ship) || []) : String(field.get(ship) ?? '-');
    console.log(`  ${index + 1}. ${field.label}: ${current}`);
  });

  const fieldIndex = await askNumber(reader, 'Field number', 1, fieldChoices.length);
  const field = fieldChoices[fieldIndex - 1];
  const current = field.kind === 'values' ? formatValues(field.get(ship) || []) : String(field.get(ship) ?? '-');
  const prompt = field.kind === 'values'
    ? `New ${field.label} values in mm, separated by / (empty keeps ${current}, - clears)`
    : `New ${field.label} in mm (empty keeps ${current}, - clears)`;
  const raw = await reader.question(`${prompt}: `);

  if (field.kind === 'values') {
    const values = parseValues(raw);
    if (values === null) {
      console.log('No change.');
      return false;
    }
    field.set(ship, values);
  } else {
    const value = parseScalar(raw);
    if (value === undefined) {
      console.log('No change.');
      return false;
    }
    field.set(ship, value);
  }

  writeDatabase(db, jsonPath);
  console.log('Database updated. JSON and Python database are in sync.');
  return true;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const jsonPath = args.db || path.join(projectRoot, 'src', 'res_mods', 'PnFMods', 'APOvermatchAssistant', 'data', 'armor_overmatch.json');
  const db = readJsonFile(jsonPath);

  if (args['self-test']) {
    const ships = Object.entries(db.ships || {});
    if (!ships.length) throw new Error('No ships found in armor database.');
    pythonLiteral({ ok: true, values: [1, 2, 3] });
    console.log(`Manual editor self-test OK. Ships: ${ships.length}`);
    return;
  }

  if (!process.stdin.isTTY) {
    throw new Error('Manual editor requires an interactive console.');
  }

  const ships = Object.entries(db.ships || {}).map(([key, ship]) => ({
    key,
    ship,
    parts: keyParts(key),
  }));

  if (!ships.length) throw new Error('No ships found in armor database.');

  console.log('AP Overmatch manual armor database editor');
  console.log(`Database: ${jsonPath}`);
  const backupPath = backupDatabase(jsonPath);
  console.log(`Backup: ${backupPath}`);

  const reader = createReader();
  try {
    let keepEditing = true;
    while (keepEditing) {
      const filters = await pickFilters(reader, ships);
      const filtered = filterShips(ships, filters);
      if (!filtered.length) {
        console.log('No ships matched those filters.');
      } else {
        const ship = await pickShip(reader, filtered);
        if (ship) await editShip(reader, db, jsonPath, ship);
      }
      keepEditing = await askYesNo(reader, 'Edit another field?', true);
    }
  } finally {
    reader.close();
  }
}

main().catch((error) => {
  console.error(`ERROR: ${error.message}`);
  process.exitCode = 1;
});
