import fs from 'node:fs';
import path from 'node:path';
import readline from 'node:readline';
import { fileURLToPath } from 'node:url';
import { normalizeApShell } from './ap-penetration.mjs';

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

function getLatestBuild(gameDir) {
  const bin = path.join(gameDir, 'bin');
  return fs.readdirSync(bin, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && /^\d+$/.test(entry.name))
    .map((entry) => entry.name)
    .sort((a, b) => Number(b) - Number(a))[0];
}

function normalizeRealm(value) {
  const normalized = String(value ?? '').replace(/\0/g, '').trim().toUpperCase();
  return /^[A-Z0-9._-]+$/.test(normalized) ? normalized : '';
}

function isDestroyerKey(shipKey) {
  return /^P[A-Z]SD/.test(String(shipKey || ''));
}

function getRealm(gameDir, explicitRealm) {
  if (explicitRealm) {
    const value = normalizeRealm(explicitRealm);
    if (value) return value;
    throw new Error(`Invalid realm value: ${explicitRealm}`);
  }

  const realmPath = path.join(gameDir, 'currentrealm.txt');
  if (fs.existsSync(realmPath)) {
    const value = normalizeRealm(fs.readFileSync(realmPath, 'utf8'));
    if (value) return value;
  }
  return 'ASIA';
}

function loadCollisionMaterialNames(projectRoot) {
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

function normalizeCaliber(value) {
  let v = Number(value);
  if (!Number.isFinite(v) || v <= 0) return null;
  if (v < 5) v *= 1000;
  else if (v < 80) v *= 10;
  return Math.round(v * 10) / 10;
}

function addUnique(list, value, maxValue = 1000) {
  const v = Math.round(Number(value) * 10) / 10;
  if (!Number.isFinite(v) || v <= 0 || v > maxValue) return;
  if (!list.includes(v)) list.push(v);
}

function sortUnique(values) {
  return [...new Set(values)].sort((a, b) => a - b);
}

function selectPrimary(values) {
  const all = sortUnique(values);
  const primary = all.filter((value) => value >= 10);
  return primary.length ? primary : all;
}

function minPositive(values) {
  const primary = selectPrimary(values);
  return primary.length ? primary[0] : null;
}

function selectPrimaryDeck(deckValues, bowValues, sternValues, sideValues) {
  const deck = selectPrimary(deckValues);
  if (!deck.length) return deck;

  const thresholds = [];
  const bowMin = minPositive(bowValues);
  const sternMin = minPositive(sternValues);
  const sideMin = minPositive(sideValues);
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
  const clean = selectPrimary(values);
  return clean.length ? clean[clean.length - 1] : 0;
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

function newArmorGroups() {
  return {
    bow: [],
    stern: [],
    deck: [],
    side: [],
    belt: [],
    bowBelt: [],
    sternBelt: [],
  };
}

function materialName(names, materialId) {
  return materialId >= 0 && materialId < names.length ? names[materialId] : `unknown_${materialId}`;
}

function isBowMaterial(name) {
  return /(^|_)Bow($|_)|Bow$|^Bow_/.test(name);
}

function isSternMaterial(name) {
  return /(^|_)St($|_)|^St_|Stern$/.test(name);
}

function addClassifiedArmor(groups, material, mm) {
  if (mm <= 0) return;
  const isBow = isBowMaterial(material);
  const isStern = isSternMaterial(material);
  const isBowOrStern = isBow || isStern;
  const platingMax = 80;
  const sideMax = 320;

  if (isBowOrStern && /Belt/.test(material)) {
    addUnique(groups.belt, mm);
    if (isBow) addUnique(groups.bowBelt, mm);
    if (isStern) addUnique(groups.sternBelt, mm);
  }

  const bowSternPlating = /ConstrSide|Deck|Fdck|SideBow|DeckBow|SideStern|DeckStern/.test(material);
  if (isBow && bowSternPlating && !/Belt|Bottom|Bulge|Inclin|Trans|Art|Cit/.test(material)) {
    addUnique(groups.bow, mm, platingMax);
  }
  if (isStern && bowSternPlating && !/Belt|Bottom|Bulge|Inclin|Trans|Art|Cit/.test(material)) {
    addUnique(groups.stern, mm, platingMax);
  }

  if (!isBowOrStern && /Deck|Fdck|Hang/.test(material) && !/Cit|OCit|Tur|Art|Bridge|Funnel|Kdp|Bottom|Trans|Inclin/.test(material)) {
    addUnique(groups.deck, mm, platingMax);
  }

  if (
    !isBowOrStern &&
    /ConstrSide|Side|Belt/.test(material) &&
    !/Cit|OCit|Tur|Art|Bridge|Funnel|Kdp|Rudder|Bulge|Bottom|SS_|SSC|SideSS/.test(material)
  ) {
    addUnique(groups.side, mm, sideMax);
  }
}

function projectileRecord(entryName, lines) {
  let ammoType = null;
  let hePen = null;
  let sapPen = null;
  let caliber = null;
  const ap = {
    shellName: entryName,
    caliberM: null,
    caliberMm: null,
    massKg: null,
    muzzleVelocityMps: null,
    krupp: null,
    airDrag: null,
    ricochetAtDeg: null,
    alwaysRicochetAtDeg: null,
    normalizationDeg: null,
    hasCap: false,
    detonatorThresholdMm: null,
    detonatorSec: null,
  };
  for (const line of lines) {
    let m = line.match(/"ammoType": "([^"]+)"/);
    if (m) ammoType = m[1];
    m = line.match(/"alphaPiercingHE": ([0-9.]+)/);
    if (m) hePen = Number(m[1]);
    m = line.match(/"alphaPiercingCS": ([0-9.]+)/);
    if (m) sapPen = Number(m[1]);
    m = line.match(/"bulletDiametr": ([0-9.]+)/);
    if (m) {
      ap.caliberM = Number(m[1]);
      caliber = normalizeCaliber(m[1]);
      ap.caliberMm = caliber;
    }
    m = line.match(/"bulletMass": ([0-9.]+)/);
    if (m) ap.massKg = Number(m[1]);
    m = line.match(/"bulletSpeed": ([0-9.]+)/);
    if (m) ap.muzzleVelocityMps = Number(m[1]);
    m = line.match(/"bulletKrupp": ([0-9.]+)/);
    if (m) ap.krupp = Number(m[1]);
    m = line.match(/"bulletAirDrag": ([0-9.]+)/);
    if (m) ap.airDrag = Number(m[1]);
    m = line.match(/"bulletRicochetAt": ([0-9.]+)/);
    if (m) ap.ricochetAtDeg = Number(m[1]);
    m = line.match(/"bulletAlwaysRicochetAt": ([0-9.]+)/);
    if (m) ap.alwaysRicochetAtDeg = Number(m[1]);
    m = line.match(/"bulletCapNormalizeMaxAngle": ([0-9.]+)/);
    if (m) ap.normalizationDeg = Number(m[1]);
    m = line.match(/"bulletCap": (true|false)/);
    if (m) ap.hasCap = m[1] === 'true';
    m = line.match(/"bulletDetonatorThreshold": ([0-9.]+)/);
    if (m) ap.detonatorThresholdMm = Number(m[1]);
    m = line.match(/"bulletDetonator": ([0-9.]+)/);
    if (m) ap.detonatorSec = Number(m[1]);
  }
  const record = {
    name: entryName,
    ammoType,
    caliberMm: caliber,
  };
  if (ammoType === 'AP') {
    const shell = normalizeApShell(ap);
    return shell ? { ...record, ap: shell } : null;
  }

  let penetration = null;
  if (ammoType === 'HE' && hePen > 0) penetration = hePen;
  else if (ammoType === 'CS' && sapPen > 0) penetration = sapPen;
  else return null;
  return {
    ...record,
    penetrationMm: Math.round(penetration * 10) / 10,
  };
}

function findMainGunPen(ammoNames, projectileMap, caliber, ammoType) {
  const values = [];
  for (const name of [...new Set(ammoNames)]) {
    const projectile = projectileMap.get(name);
    if (!projectile || projectile.ammoType !== ammoType) continue;
    if (caliber && projectile.caliberMm && Math.abs(projectile.caliberMm - caliber) > 2) continue;
    addUnique(values, projectile.penetrationMm);
  }
  if (!values.length && caliber) {
    for (const name of [...new Set(ammoNames)]) {
      const projectile = projectileMap.get(name);
      if (!projectile || projectile.ammoType !== ammoType) continue;
      addUnique(values, projectile.penetrationMm);
    }
  }
  return values.length ? sortUnique(values).at(-1) : null;
}

function findMainGunAp(ammoNames, projectileMap, caliber) {
  const candidates = [];
  for (const name of [...new Set(ammoNames)]) {
    const projectile = projectileMap.get(name);
    if (!projectile || projectile.ammoType !== 'AP' || !projectile.ap) continue;
    if (caliber && projectile.caliberMm && Math.abs(projectile.caliberMm - caliber) > 2) continue;
    candidates.push(projectile.ap);
  }
  if (!candidates.length && caliber) {
    for (const name of [...new Set(ammoNames)]) {
      const projectile = projectileMap.get(name);
      if (projectile && projectile.ammoType === 'AP' && projectile.ap) candidates.push(projectile.ap);
    }
  }
  if (!candidates.length) return null;
  candidates.sort((a, b) => {
    const aPen = a.table?.[0]?.verticalPenetrationMm || 0;
    const bPen = b.table?.[0]?.verticalPenetrationMm || 0;
    return bPen - aPen;
  });
  return candidates[0];
}

function collectMainGunStats(lines) {
  const stack = [];
  const calibers = [];
  const ammoNames = [];
  let depth = 0;

  function nearestGunCandidate() {
    for (let i = stack.length - 1; i >= 0; i--) {
      const ctx = stack[i];
      if (ctx.barrelDiameter || ctx.ammoNames.length) return ctx;
    }
    return null;
  }

  function closeContext(ctx) {
    if (ctx.barrelDiameter && ctx.species === 'Main' && ctx.type === 'Gun') {
      addUnique(calibers, ctx.barrelDiameter, 600);
      for (const name of ctx.ammoNames) {
        if (!ammoNames.includes(name)) ammoNames.push(name);
      }
    }
  }

  for (const line of lines) {
    const beforeDepth = depth;
    const open = line.match(/^\s+"([^"]+)": \{/);
    if (open) {
      stack.push({
        name: open[1],
        depth: beforeDepth + 1,
        barrelDiameter: null,
        ammoNames: [],
        collectingAmmo: false,
        ammoDepth: 0,
        species: null,
        type: null,
      });
    }

    const top = stack.at(-1);
    if (top && /"ammoList": \[/.test(line)) {
      top.collectingAmmo = true;
      top.ammoDepth = beforeDepth + jsonDepthDelta(line);
    }

    for (let i = stack.length - 1; i >= 0; i--) {
      const ctx = stack[i];
      if (!ctx.collectingAmmo) continue;
      const ammo = line.match(/^\s+"([^"]+)"[,]?$/);
      if (ammo && !ctx.ammoNames.includes(ammo[1])) ctx.ammoNames.push(ammo[1]);
      break;
    }

    let m = line.match(/"barrelDiameter": ([0-9.]+)/);
    if (m && top) top.barrelDiameter = normalizeCaliber(m[1]);

    m = line.match(/"species": "([^"]+)"/);
    if (m) {
      const candidate = nearestGunCandidate();
      if (candidate) candidate.species = m[1];
    }

    m = line.match(/"type": "([^"]+)"/);
    if (m) {
      const candidate = nearestGunCandidate();
      if (candidate) candidate.type = m[1];
    }

    const nextDepth = depth + jsonDepthDelta(line);
    for (const ctx of stack) {
      if (ctx.collectingAmmo && nextDepth < ctx.ammoDepth) ctx.collectingAmmo = false;
    }
    while (stack.length && nextDepth < stack.at(-1).depth) {
      closeContext(stack.pop());
    }
    depth = nextDepth;
  }

  while (stack.length) closeContext(stack.pop());
  const sortedCalibers = sortUnique(calibers);
  return {
    maxCaliber: sortedCalibers.length ? sortedCalibers.at(-1) : null,
    ammoNames,
  };
}

async function collectProjectilePenetration(gameParamsPath) {
  const projectileMap = new Map();
  const stream = fs.createReadStream(gameParamsPath, { encoding: 'utf8' });
  const rl = readline.createInterface({ input: stream, crlfDelay: Infinity });
  let capturing = false;
  let depth = 0;
  let entryName = null;
  let lines = [];

  for await (const line of rl) {
    if (!capturing) {
      const m = line.match(/^  "([^"]+)": \{/);
      if (m && /^[A-Z][A-Z]P[A-Z]\d+/.test(m[1])) {
        capturing = true;
        depth = 0;
        entryName = m[1];
        lines = [line];
        depth += jsonDepthDelta(line);
      }
    } else {
      lines.push(line);
      depth += jsonDepthDelta(line);
    }

    if (capturing && depth === 0) {
      const record = projectileRecord(entryName, lines);
      if (record) projectileMap.set(entryName, record);
      capturing = false;
      entryName = null;
      lines = [];
    }
  }
  return projectileMap;
}

function shipRecord(entryName, lines, projectileMap, materialNames) {
  let isShip = false;
  let name = entryName;
  let index = null;
  let id = null;
  let originShipName = '';
  let unpeculiarShip = '';
  let shipModel = '';
  const mainGunStats = collectMainGunStats(lines);
  const maxCaliber = mainGunStats.maxCaliber;
  const ammoNames = mainGunStats.ammoNames;
  let selectedGroups = newArmorGroups();
  let currentGroups = null;
  let inHull = false;
  let hullDepth = 0;
  let inArmor = false;
  let armorDepth = 0;

  for (const line of lines) {
    if (/^\s+"type": "Ship"/.test(line)) isShip = true;
    let m = line.match(/^    "name": "([^"]+)"/);
    if (m) name = m[1];
    m = line.match(/^    "index": "([^"]+)"/);
    if (m) index = m[1];
    m = line.match(/^    "id": ([0-9]+)/);
    if (m) id = m[1];
    m = line.match(/^    "originShipName": "([^"]*)"/);
    if (m) originShipName = m[1];
    m = line.match(/^    "unpeculiarShip": "([^"]*)"/);
    if (m) unpeculiarShip = m[1];
    m = line.match(/^\s+"model": "([^"]*\/ship\/[^"]+\.model)"/);
    if (m && !shipModel) shipModel = m[1];

    if (!inHull) {
      m = line.match(/^    "([^"]*Hull[^"]*)": \{/);
      if (m) {
        inHull = true;
        hullDepth = 0;
        currentGroups = newArmorGroups();
      }
    }
    if (inHull && !inArmor && /^      "armor": \{/.test(line)) {
      inArmor = true;
      armorDepth = 0;
    } else if (inArmor) {
      m = line.match(/^        "([0-9]+)": ([0-9.]+)/);
      if (m) {
        const rawKey = Number(m[1]);
        const mm = Number(m[2]);
        if (Number.isFinite(rawKey) && Number.isFinite(mm)) {
          const matId = rawKey % 65536;
          addClassifiedArmor(currentGroups, materialName(materialNames, matId), mm);
        }
      }
    }

    if (inArmor) {
      armorDepth += jsonDepthDelta(line);
      if (armorDepth === 0) inArmor = false;
    }
    if (inHull) {
      hullDepth += jsonDepthDelta(line);
      if (hullDepth === 0) {
        selectedGroups = currentGroups;
        currentGroups = null;
        inHull = false;
        inArmor = false;
      }
    }
  }

  if (!isShip) return null;
  const aliases = [];
  for (const alias of [entryName, index, id, name]) {
    if (alias && !aliases.includes(String(alias))) aliases.push(String(alias));
  }

  const extendedBelt = selectExtendedBowSternBelt(
    selectedGroups.bowBelt,
    selectedGroups.sternBelt,
    selectedGroups.bow,
    selectedGroups.stern,
  );
  const sideValues = selectPrimarySide(selectedGroups.side, selectedGroups.belt);
  const mainBeltValues = isDestroyerKey(entryName) ? [] : sideValues;

  return {
    name: String(name),
    aliases,
    mainGunCaliberMm: maxCaliber,
    mainGunHePenMm: findMainGunPen(ammoNames, projectileMap, maxCaliber, 'HE'),
    mainGunSapPenMm: findMainGunPen(ammoNames, projectileMap, maxCaliber, 'CS'),
    mainGunAp: findMainGunAp(ammoNames, projectileMap, maxCaliber),
    _originShipName: originShipName,
    _unpeculiarShip: unpeculiarShip,
    _shipModel: shipModel,
    armor: {
      bowStern: {
        bow: selectPrimary(selectedGroups.bow),
        stern: selectPrimary(selectedGroups.stern),
      },
      deck: { values: selectPrimaryDeck(selectedGroups.deck, selectedGroups.bow, selectedGroups.stern, sideValues) },
      side: { values: sideValues },
      mainBelt: {
        values: mainBeltValues,
        inclinationDeg: {
          min: 0,
          max: 0,
          estimated: true,
        },
        headingAngleDeg: {
          min: 0,
          max: 0,
          estimated: true,
        },
      },
      extendedBowSternBelt: {
        present: extendedBelt.values.length > 0,
        values: extendedBelt.values,
        bow: extendedBelt.bow,
        stern: extendedBelt.stern,
      },
    },
  };
}

function hasMainGunStats(ship) {
  return Number(ship?.mainGunCaliberMm) > 0;
}

function copyMissingMainGunStats(target, source) {
  if (!target || !source || !hasMainGunStats(source)) return false;
  let changed = false;
  for (const field of ['mainGunCaliberMm', 'mainGunHePenMm', 'mainGunSapPenMm', 'mainGunAp']) {
    if (target[field] == null && source[field] != null) {
      target[field] = source[field];
      changed = true;
    }
  }
  return changed;
}

function resolveDerivedShipMainGuns(ships) {
  const aliases = new Map();
  for (const [key, ship] of Object.entries(ships)) {
    aliases.set(key, key);
    for (const alias of ship.aliases || []) aliases.set(String(alias), key);
  }

  const modelStats = new Map();
  for (const [key, ship] of Object.entries(ships)) {
    if (!ship._shipModel || !hasMainGunStats(ship)) continue;
    const stats = {
      mainGunCaliberMm: ship.mainGunCaliberMm,
      mainGunHePenMm: ship.mainGunHePenMm,
      mainGunSapPenMm: ship.mainGunSapPenMm,
      mainGunAp: ship.mainGunAp,
    };
    const signature = JSON.stringify(stats);
    if (!modelStats.has(ship._shipModel)) modelStats.set(ship._shipModel, new Map());
    modelStats.get(ship._shipModel).set(signature, { key, stats });
  }

  let changedCount = 0;
  for (let pass = 0; pass < 4; pass++) {
    let passChanged = false;
    for (const [key, ship] of Object.entries(ships)) {
      if (hasMainGunStats(ship)) continue;

      for (const fallback of [ship._originShipName, ship._unpeculiarShip]) {
        if (!fallback || fallback === key) continue;
        const sourceKey = aliases.get(String(fallback));
        if (sourceKey && copyMissingMainGunStats(ship, ships[sourceKey])) {
          changedCount++;
          passChanged = true;
          break;
        }
      }
      if (hasMainGunStats(ship)) continue;

      const byModel = modelStats.get(ship._shipModel);
      if (byModel && byModel.size === 1) {
        const [{ stats }] = [...byModel.values()];
        if (copyMissingMainGunStats(ship, stats)) {
          changedCount++;
          passChanged = true;
        }
      }
    }
    if (!passChanged) break;
  }

  for (const ship of Object.values(ships)) {
    delete ship._originShipName;
    delete ship._unpeculiarShip;
    delete ship._shipModel;
  }

  return changedCount;
}

async function collectShips(gameParamsPath, projectileMap, materialNames, shipKeyFilter, maxShips) {
  const ships = {};
  const stream = fs.createReadStream(gameParamsPath, { encoding: 'utf8' });
  const rl = readline.createInterface({ input: stream, crlfDelay: Infinity });
  let capturing = false;
  let depth = 0;
  let entryName = null;
  let lines = [];

  for await (const line of rl) {
    if (!capturing) {
      const m = line.match(/^  "([^"]+)": \{/);
      if (m) {
        const candidate = m[1];
        const isShipKey = /^P[A-Z]S[A-Z]/.test(candidate);
        const matchesFilter = !shipKeyFilter || wildcardMatch(candidate, shipKeyFilter);
        if (isShipKey && matchesFilter) {
          capturing = true;
          depth = 0;
          entryName = candidate;
          lines = [line];
          depth += jsonDepthDelta(line);
        }
      }
    } else {
      lines.push(line);
      depth += jsonDepthDelta(line);
    }

    if (capturing && depth === 0) {
      const record = shipRecord(entryName, lines, projectileMap, materialNames);
      if (record) {
        ships[entryName] = record;
        const count = Object.keys(ships).length;
        if (count % 50 === 0) console.log(`  parsed ${count} ships...`);
      }
      capturing = false;
      entryName = null;
      lines = [];
      if (maxShips > 0 && Object.keys(ships).length >= maxShips) break;
    }
  }
  const derivedCount = resolveDerivedShipMainGuns(ships);
  if (derivedCount) console.log(`Resolved main-gun data for ${derivedCount} derived ships.`);
  return ships;
}

function wildcardMatch(value, pattern) {
  const escaped = pattern.replace(/[.+^${}()|[\]\\]/g, '\\$&').replace(/\*/g, '.*').replace(/\?/g, '.');
  return new RegExp(`^${escaped}$`, 'i').test(value);
}

function applyOverrides(ships, overridePath) {
  if (!overridePath || !fs.existsSync(overridePath)) return;
  console.log(`Applying overrides from ${overridePath}...`);
  const overrides = readJsonFile(overridePath);
  if (!overrides.ships) return;
  for (const [key, value] of Object.entries(overrides.ships)) ships[key] = value;
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
  return pyOutPath;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const projectRoot = args['project-root'] || path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
  const gameDir = args['game-dir'];
  const gameParamsJson = args['game-params-json'];
  const outPath = args['out-path'];
  if (!gameDir || !gameParamsJson || !outPath) {
    throw new Error('Required args: --game-dir, --game-params-json, --out-path');
  }
  const build = getLatestBuild(gameDir);
  const realm = getRealm(gameDir, args.realm);
  const materialNames = loadCollisionMaterialNames(projectRoot);

  console.log(`Streaming ${gameParamsJson} with fast Node parser...`);
  const projectileMap = await collectProjectilePenetration(gameParamsJson);
  console.log(`Collected ${projectileMap.size} projectile records.`);
  const ships = await collectShips(
    gameParamsJson,
    projectileMap,
    materialNames,
    args['ship-key-filter'] || '',
    Number(args['max-ships'] || 0),
  );
  applyOverrides(ships, args['override-path']);

  const database = {
    schema: 3,
    meta: {
      name: '14.3-helper',
      gameBuild: build,
      realm,
      generatedAt: new Date().toISOString().slice(0, 19),
      source: 'wowsunpack GameParams JSON, streamed per ship',
      notes: 'Armor groups are classified from collision material IDs. Deck uses a representative weather-deck thickness rather than every deck-like material. Side/mainBelt uses side belt-like materials as a first-pass main belt proxy. Main-gun HE/SAP penetration is resolved from projectile alphaPiercingHE/alphaPiercingCS. Main-gun AP stores unpacked shell parameters and a deterministic approximate penetration table for in-battle main-belt checks.',
    },
    ships,
  };

  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  const jsonText = JSON.stringify(database, null, 2);
  fs.writeFileSync(outPath, jsonText, 'utf8');
  const pyOutPath = writePythonDatabase(database, outPath);
  console.log(`Wrote ${Object.keys(ships).length} ships to ${outPath}`);
  console.log(`Wrote Python database to ${pyOutPath}`);
}

main().catch((error) => {
  console.error(error && error.stack ? error.stack : String(error));
  process.exit(1);
});
