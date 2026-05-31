import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const projectRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const jsonPath = process.argv[2] || path.join(
  projectRoot,
  'src',
  'res_mods',
  'PnFMods',
  'APOvermatchAssistant',
  'data',
  'armor_overmatch.json',
);

function readJsonFile(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8').replace(/^\uFEFF/, ''));
}

function sortUnique(values) {
  return [...new Set((values || []).map(Number).filter((value) => Number.isFinite(value) && value > 0))]
    .sort((a, b) => a - b);
}

function zeroEstimatedAngleRange() {
  return { min: 0, max: 0, estimated: true };
}

function normalizeAngleRange(range) {
  const min = Number(range?.min);
  const max = Number(range?.max);
  const hasMeasuredRange = range?.estimated === false && Number.isFinite(min) && Number.isFinite(max);
  if (!hasMeasuredRange) return zeroEstimatedAngleRange();
  return {
    min,
    max,
    estimated: false,
  };
}

function selectPrimary(values) {
  const all = sortUnique(values);
  const primary = all.filter((value) => value >= 10);
  return primary.length ? primary : all;
}

function minPrimary(values) {
  const primary = selectPrimary(values);
  return primary.length ? primary[0] : null;
}

function selectPrimaryDeck(deckValues, bowValues, sternValues, sideValues) {
  const deck = selectPrimary(deckValues);
  if (!deck.length) return deck;

  const thresholds = [];
  const bowMin = minPrimary(bowValues);
  const sternMin = minPrimary(sternValues);
  const sideMin = minPrimary(sideValues);
  if (bowMin) thresholds.push(bowMin);
  if (sternMin) thresholds.push(sternMin);
  if (sideMin && sideMin <= 40) thresholds.push(sideMin);

  const threshold = thresholds.length ? Math.max(...thresholds) : 10;
  const primaryDeck = deck.find((value) => value >= threshold);
  return [primaryDeck || deck[0]];
}

function selectPrimarySide(sideValues, beltValues) {
  const side = selectPrimary(sideValues);
  if (side.length) return side;
  return [];
}

function maxValue(values) {
  const primary = selectPrimary(values);
  return primary.length ? primary[primary.length - 1] : 0;
}

function strongestValue(values) {
  const max = maxValue(values);
  return max ? [max] : [];
}

function selectExtendedBowSternBelt(bowBeltValues, sternBeltValues, bowValues, sternValues) {
  const bow = selectPrimary(bowBeltValues);
  const stern = selectPrimary(sternBeltValues);
  return {
    values: sortUnique([...bow, ...stern]),
    bow,
    stern,
  };
}

const SIDE_VALUE_OVERRIDES = {
  PGSC108_Hipper: [27],
  PGSC508_Prinz_Eugen: [27],
  PGSC518_Mainz: [25],
  PGSC598_Black_Mainz: [25],
  PGSC729_Blucher: [27],
  PGSB207_Prinz_Heinrich: [150],
  PGSB517_AZUR_Prinz_Heinrich: [150],
  PGSB108_Bismarck: [160],
  PGSB598_Black_Tirpitz: [160],
  PGSB708_Bismarck_1941: [160],
  PGSB818_BA_Tirpitz: [160],
  PGSB898_Azur_Bismarck: [160],
  PXSB005_Bismarck_H2017: [160],
};

function sameValues(left, right) {
  return left.length === right.length && left.every((value, index) => value === right[index]);
}

function sameAngleRange(left = {}, right = {}) {
  return Number(left.min || 0) === Number(right.min || 0) &&
    Number(left.max || 0) === Number(right.max || 0) &&
    Boolean(left.estimated) === Boolean(right.estimated);
}

function sameMainBelt(left = {}, right = {}) {
  return sameValues(sortUnique(left.values || []), sortUnique(right.values || [])) &&
    sameAngleRange(left.inclinationDeg || {}, right.inclinationDeg || {}) &&
    sameAngleRange(left.headingAngleDeg || {}, right.headingAngleDeg || {});
}

function normalizeMainBelt(mainBelt = {}, sideValues = []) {
  const values = sortUnique(mainBelt.values || []);
  const hasMeasuredGeometry = values.length > 0 &&
    mainBelt.inclinationDeg?.estimated === false &&
    mainBelt.headingAngleDeg?.estimated === false;
  const fallbackValues = hasMeasuredGeometry ? values : strongestValue(values.length ? values : sideValues);
  return {
    values: fallbackValues,
    inclinationDeg: hasMeasuredGeometry ? normalizeAngleRange(mainBelt.inclinationDeg) : zeroEstimatedAngleRange(),
    headingAngleDeg: hasMeasuredGeometry ? normalizeAngleRange(mainBelt.headingAngleDeg) : zeroEstimatedAngleRange(),
  };
}

function pythonLiteral(value, depth = 0) {
  const indent = '  '.repeat(depth);
  const nextIndent = '  '.repeat(depth + 1);
  if (value === null) return 'None';
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
  const pyLiteral = pythonLiteral(database);
  const pyText = `# -*- coding: utf-8 -*-\n# Generated from armor_overmatch.json. WoWS ModsAPI blocks the json module.\nDATABASE = ${pyLiteral}\n`;
  fs.writeFileSync(pyOutPath, pyText, 'utf8');
}

const db = readJsonFile(jsonPath);
let changedDeck = 0;
let changedSide = 0;
let changedBelt = 0;
let changedMainBelt = 0;

for (const [shipKey, ship] of Object.entries(db.ships || {})) {
  const armor = ship.armor || {};
  const bowStern = armor.bowStern || {};
  const side = armor.side || {};
  const belt = armor.extendedBowSternBelt || {};
  const nextSide = SIDE_VALUE_OVERRIDES[shipKey] || selectPrimarySide(side.values || [], belt.values || []);
  const currentSide = sortUnique(side.values || []);
  if (!sameValues(currentSide, nextSide)) {
    side.values = nextSide;
    armor.side = side;
    ship.armor = armor;
    changedSide++;
  }

  const nextMainBelt = normalizeMainBelt(armor.mainBelt || {}, armor.side?.values || []);
  if (!sameMainBelt(armor.mainBelt || {}, nextMainBelt)) {
    armor.mainBelt = nextMainBelt;
    ship.armor = armor;
    changedMainBelt++;
  }

  const nextBelt = selectExtendedBowSternBelt(
    belt.bow || [],
    belt.stern || [],
    bowStern.bow || [],
    bowStern.stern || [],
  );
  const currentBelt = sortUnique(belt.values || []);
  const currentBowBelt = sortUnique(belt.bow || []);
  const currentSternBelt = sortUnique(belt.stern || []);
  if (
    Boolean(belt.present) !== (nextBelt.values.length > 0) ||
    !sameValues(currentBelt, nextBelt.values) ||
    !sameValues(currentBowBelt, nextBelt.bow) ||
    !sameValues(currentSternBelt, nextBelt.stern)
  ) {
    belt.present = nextBelt.values.length > 0;
    belt.values = nextBelt.values;
    belt.bow = nextBelt.bow;
    belt.stern = nextBelt.stern;
    armor.extendedBowSternBelt = belt;
    ship.armor = armor;
    changedBelt++;
  }

  const deck = armor.deck || {};
  const next = selectPrimaryDeck(
    deck.values || [],
    bowStern.bow || [],
    bowStern.stern || [],
    armor.side?.values || [],
  );

  const current = sortUnique(deck.values || []);
  if (!sameValues(current, next)) {
    deck.values = next;
    armor.deck = deck;
    ship.armor = armor;
    changedDeck++;
  }
}

if (db.meta) {
  const note = 'Deck uses a representative weather-deck thickness rather than every deck-like material. Side means upper side plating above the main armor belt. Main belt records without measured geometry keep a complete 0 degree estimated angle range, and ships with side armor but no main belt fall back to side armor. Known armor-viewer corrections are applied for ships whose side material is not separable from client collision material groups.';
  db.meta.notes = db.meta.notes && !db.meta.notes.includes(note)
    ? `${note} ${db.meta.notes}`
    : (db.meta.notes || note);
}

const jsonText = `${JSON.stringify(db, null, 2)}\n`;
fs.writeFileSync(jsonPath, jsonText, 'utf8');
writePythonDatabase(db, jsonPath);

const hindenburg = db.ships?.PGSC110_Hindenburg?.armor?.deck?.values || [];
const prinzHeinrich = db.ships?.PGSB207_Prinz_Heinrich?.armor?.side?.values || [];
const azurPrinzHeinrich = db.ships?.PGSB517_AZUR_Prinz_Heinrich?.armor?.side?.values || [];
console.log(`Normalized deck values for ${changedDeck} ships.`);
console.log(`Normalized side values for ${changedSide} ships.`);
console.log(`Normalized extended belt values for ${changedBelt} ships.`);
console.log(`Normalized main belt fallback geometry for ${changedMainBelt} ships.`);
console.log(`PGSC110_Hindenburg deck: ${hindenburg.join('/') || '?'}`);
console.log(`PGSB207_Prinz_Heinrich side: ${prinzHeinrich.join('/') || '?'}`);
console.log(`PGSB517_AZUR_Prinz_Heinrich side: ${azurPrinzHeinrich.join('/') || '?'}`);
