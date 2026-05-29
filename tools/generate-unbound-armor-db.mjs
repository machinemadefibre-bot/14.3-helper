import fs from 'node:fs';
import path from 'node:path';

const projectRoot = path.resolve(import.meta.dirname, '..');
const jsonPath = path.join(projectRoot, 'src', 'res_mods', 'PnFMods', 'APOvermatchAssistant', 'data', 'armor_overmatch.json');
const unboundPath = path.join(projectRoot, 'src', 'res_mods', 'gui', 'unbound2', 'PnFMods', 'APOvermatchAssistant.unbound');

function readJsonFile(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8').replace(/^\uFEFF/, ''));
}

const db = readJsonFile(jsonPath);

function unique(values) {
  return [...new Set((values || []).map(Number).filter((value) => Number.isFinite(value) && value > 0))].sort((a, b) => a - b);
}

function flatten(group) {
  if (!group) return [];
  if (Array.isArray(group)) return unique(group);
  if (typeof group === 'object') {
    const result = [];
    for (const key of ['values', 'bow', 'stern', 'fore', 'aft', 'main']) {
      const item = group[key];
      if (Array.isArray(item)) result.push(...item);
      else if (item != null) result.push(item);
    }
    return unique(result);
  }
  return unique([group]);
}

function formatMm(values) {
  const clean = unique(values);
  if (!clean.length) return '? mm';
  return clean.map((value) => Math.abs(value - Math.round(value)) < 0.01 ? `${Math.round(value)} mm` : `${value.toFixed(1)} mm`).join('/');
}

function section(values) {
  const clean = unique(values);
  return {
    min: clean.length ? clean[0] : 0,
    max: clean.length ? clean[clean.length - 1] : 0,
    text: formatMm(clean),
  };
}

function literalString(value) {
  return `'${String(value ?? '').replace(/\\/g, '\\\\').replace(/'/g, "\\'")}'`;
}

function numeric(value) {
  const num = Number(value);
  return Number.isFinite(num) ? Number(num.toFixed(3)) : 0;
}

function numericArray(values) {
  return `[${(values || []).map(numeric).join(',')}]`;
}

function shipTypeCode(key) {
  const match = String(key || '').match(/^P[A-Z]S([ABCDS])/);
  return match ? match[1] : '';
}

const records = {};
const aliases = {};
for (const [name, ship] of Object.entries(db.ships || {})) {
  const numericAlias = (ship.aliases || []).find((alias) => /^\d+$/.test(String(alias)));
  if (!numericAlias) continue;
  const typeCode = shipTypeCode(name);

  const armor = ship.armor || {};
  const bowStern = armor.bowStern || {};
  const bow = section(flatten(bowStern.bow || bowStern.fore || bowStern.values || bowStern));
  const stern = section(flatten(bowStern.stern || bowStern.aft || bowStern.values || bowStern));
  const deck = section(flatten(armor.deck));
  const side = section(flatten(armor.side));
  const mainBelt = armor.mainBelt || {};
  const mainBeltSource = typeCode === 'D' ? [] : (mainBelt.values || mainBelt || armor.side);
  const mainBeltSection = section(flatten(mainBeltSource));
  const inclination = mainBelt.inclinationDeg || {};
  const headingAngle = mainBelt.headingAngleDeg || {};
  const ap = ship.mainGunAp || {};
  const apTable = Array.isArray(ap.table) ? ap.table : [];
  const apVerticalPen = apTable.map((row) => row.verticalPenetrationMm);
  const apHorizontalPen = apTable.map((row) => row.horizontalPenetrationMm);
  const apImpactAngle = apTable.map((row) => row.impactAngleDeg);

  const beltGroup = armor.extendedBowSternBelt || {};
  const beltBowValues = flatten(beltGroup.bow || beltGroup.fore || []);
  const beltSternValues = flatten(beltGroup.stern || beltGroup.aft || []);
  const legacyBeltValues = beltBowValues.length || beltSternValues.length ? [] : flatten(beltGroup);
  const beltBow = section(beltBowValues);
  const beltStern = section(beltSternValues);
  const beltValues = unique([...beltBowValues, ...beltSternValues, ...legacyBeltValues]);
  const belt = section(beltValues);
  const beltBowPresent = beltBowValues.length > 0;
  const beltSternPresent = beltSternValues.length > 0;
  const beltPresent = Boolean(beltGroup.present) && (beltBowPresent || beltSternPresent || beltValues.length > 0);

  const recordKey = String(numericAlias);
  const aliasKeys = [name, ship.name, ...(ship.aliases || [])]
    .map((value) => String(value ?? '').trim())
    .filter(Boolean);
  for (const alias of aliasKeys) {
    aliases[alias] = recordKey;
  }

  records[recordKey] = {
    n: ship.name || name,
    ty: typeCode,
    c: numeric(ship.mainGunCaliberMm),
    he: numeric(ship.mainGunHePenMm),
    sap: numeric(ship.mainGunSapPenMm),
    apv: apVerticalPen,
    aph: apHorizontalPen,
    api: apImpactAngle,
    ar: numeric(ap.ricochetAtDeg),
    aa: numeric(ap.alwaysRicochetAtDeg),
    an: numeric(ap.normalizationDeg),
    bmn: bow.min,
    bmx: bow.max,
    bt: bow.text,
    smn: stern.min,
    smx: stern.max,
    st: stern.text,
    dmn: deck.min,
    dmx: deck.max,
    dt: deck.text,
    xmn: side.min,
    xmx: side.max,
    xt: side.text,
    mbmn: mainBeltSection.min,
    mbmx: mainBeltSection.max,
    mbt: mainBeltSection.text,
    imn: numeric(inclination.min),
    imx: numeric(inclination.max),
    ie: Boolean(inclination.estimated),
    hmn: numeric(headingAngle.min),
    hmx: numeric(headingAngle.max),
    hie: Boolean(headingAngle.estimated),
    bp: beltPresent,
    bbp: beltBowPresent,
    bbmn: beltBow.min,
    bbmx: beltBow.max,
    bbt: beltBow.text,
    bsp: beltSternPresent,
    bsmn: beltStern.min,
    bsmx: beltStern.max,
    bst: beltStern.text,
    blmn: belt.min,
    blmx: belt.max,
    blt: belt.text,
  };
}

const lines = [
  '# BEGIN GENERATED ARMOR DB - run tools/generate-unbound-armor-db.mjs',
  `(def constant OA_ARMOR_DB_BUILD ${literalString(db.meta?.gameBuild || '')})`,
  '(def constant OA_ARMOR_DB {',
];

for (const [id, rec] of Object.entries(records).sort((a, b) => Number(a[0]) - Number(b[0]))) {
  lines.push(
    `  '${id}': {n:${literalString(rec.n)}, ty:${literalString(rec.ty)}, c:${rec.c}, he:${rec.he}, sap:${rec.sap}, ` +
    `apv:${numericArray(rec.apv)}, aph:${numericArray(rec.aph)}, api:${numericArray(rec.api)}, ar:${rec.ar}, aa:${rec.aa}, an:${rec.an}, ` +
    `bmn:${rec.bmn}, bmx:${rec.bmx}, bt:${literalString(rec.bt)}, smn:${rec.smn}, smx:${rec.smx}, st:${literalString(rec.st)}, ` +
    `dmn:${rec.dmn}, dmx:${rec.dmx}, dt:${literalString(rec.dt)}, xmn:${rec.xmn}, xmx:${rec.xmx}, xt:${literalString(rec.xt)}, ` +
    `mbmn:${rec.mbmn}, mbmx:${rec.mbmx}, mbt:${literalString(rec.mbt)}, imn:${rec.imn}, imx:${rec.imx}, ie:${rec.ie ? 'true' : 'false'}, ` +
    `hmn:${rec.hmn}, hmx:${rec.hmx}, hie:${rec.hie ? 'true' : 'false'}, ` +
    `bp:${rec.bp ? 'true' : 'false'}, bbp:${rec.bbp ? 'true' : 'false'}, bbmn:${rec.bbmn}, bbmx:${rec.bbmx}, bbt:${literalString(rec.bbt)}, ` +
    `bsp:${rec.bsp ? 'true' : 'false'}, bsmn:${rec.bsmn}, bsmx:${rec.bsmx}, bst:${literalString(rec.bst)}, ` +
    `blmn:${rec.blmn}, blmx:${rec.blmx}, blt:${literalString(rec.blt)}},`
  );
}

lines.push('})', '(def constant OA_ARMOR_ALIAS {');
for (const [alias, id] of Object.entries(aliases).sort((a, b) => a[0].localeCompare(b[0]))) {
  if (alias === id) continue;
  lines.push(`  ${literalString(alias)}: ${literalString(id)},`);
}

lines.push('})', '# END GENERATED ARMOR DB');
const block = `${lines.join('\n')}\n\n`;

let unbound = fs.readFileSync(unboundPath, 'utf8');
const begin = '# BEGIN GENERATED ARMOR DB';
const end = '# END GENERATED ARMOR DB';
const beginIndex = unbound.indexOf(begin);
const endIndex = unbound.indexOf(end);

if (beginIndex >= 0 && endIndex >= beginIndex) {
  const afterEnd = unbound.indexOf('\n', endIndex);
  const replaceEnd = afterEnd >= 0 ? afterEnd + 1 : unbound.length;
  unbound = unbound.slice(0, beginIndex) + block + unbound.slice(replaceEnd).replace(/^\n+/, '');
} else {
  const insertAt = unbound.indexOf('\n\n');
  unbound = unbound.slice(0, insertAt + 2) + block + unbound.slice(insertAt + 2);
}

fs.writeFileSync(unboundPath, unbound, 'utf8');
console.log(`Wrote ${Object.keys(records).length} armor records and ${Object.keys(aliases).length} aliases to ${unboundPath}`);
