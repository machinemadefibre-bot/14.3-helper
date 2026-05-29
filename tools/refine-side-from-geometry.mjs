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

function sortUnique(values) {
  return [...new Set((values || []).map(Number).filter((value) => Number.isFinite(value) && value > 0))]
    .sort((a, b) => a - b);
}

function selectPrimary(values) {
  const all = sortUnique(values);
  const primary = all.filter((value) => value >= 10);
  return primary.length ? primary : all;
}

function primaryVisible(values) {
  return selectPrimary(values).filter((value) => value >= 10);
}

function sameValues(left, right) {
  return left.length === right.length && left.every((value, index) => value === right[index]);
}

function isDestroyerKey(shipKey) {
  return /^P[A-Z]SD/.test(shipKey);
}

function isSubmarineKey(shipKey) {
  return /^P[A-Z]SS/.test(shipKey);
}

function maxValue(values) {
  return values.length ? values[values.length - 1] : 0;
}

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

function isBowMaterial(name) {
  return /(^|_)Bow($|_)|Bow$|^Bow_/.test(name);
}

function isSternMaterial(name) {
  return /(^|_)St($|_)|^St_|Stern$/.test(name);
}

function isSideCandidate(materialName) {
  const bowOrStern = isBowMaterial(materialName) || isSternMaterial(materialName);
  return !bowOrStern &&
    /ConstrSide|Side|Belt/.test(materialName) &&
    !/Cit|OCit|Tur|Art|Bridge|Funnel|Kdp|Rudder|Bulge|Bottom|SS_|SSC|SideSS/.test(materialName);
}

function isCarrierKey(shipKey) {
  return /^P[A-Z]SA/.test(shipKey);
}

function isBowSternPlatingCandidate(materialName) {
  return /ConstrSide|Deck|Fdck|SideBow|DeckBow|SideStern|DeckStern/.test(materialName) &&
    !/Belt|Bottom|Bulge|Inclin|Trans|Art|Cit|OCit|SS_|SSC|SideSS/.test(materialName);
}

function isDeckCandidate(materialName) {
  const bowOrStern = isBowMaterial(materialName) || isSternMaterial(materialName);
  return !bowOrStern &&
    /Deck|Fdck|Hang/.test(materialName) &&
    !/Cit|OCit|Tur|Art|Bridge|Funnel|Kdp|Bottom|Trans|Inclin|SS_|SideSS/.test(materialName);
}

function isCarrierDeckCandidate(materialName) {
  return /Deck|Fdck|Hang/.test(materialName) &&
    !/Cit|OCit|Tur|Art|Bridge|Funnel|Kdp|Bottom|Trans|Inclin|SideSS/.test(materialName);
}

function isCarrierSideCandidate(materialName) {
  const bowOrStern = isBowMaterial(materialName) || isSternMaterial(materialName);
  return !bowOrStern &&
    /ConstrSide|Side/.test(materialName) &&
    !/Belt|Cit|OCit|Tur|Art|Bridge|Funnel|Kdp|Rudder|Bulge|Bottom|SS_Side|SideSS|Deck|Trans|Inclin/.test(materialName);
}

function includePoint(bounds, vertex) {
  for (let i = 0; i < 3; i++) {
    bounds.min[i] = Math.min(bounds.min[i], vertex[i]);
    bounds.max[i] = Math.max(bounds.max[i], vertex[i]);
  }
}

function newSurfaceBounds() {
  return {
    count: 0,
    area: 0,
    min: [Number.POSITIVE_INFINITY, Number.POSITIVE_INFINITY, Number.POSITIVE_INFINITY],
    max: [Number.NEGATIVE_INFINITY, Number.NEGATIVE_INFINITY, Number.NEGATIVE_INFINITY],
    inclinationHistogram: [],
    headingHistogram: [],
  };
}

function newBounds() {
  return {
    count: 0,
    area: 0,
    min: [Number.POSITIVE_INFINITY, Number.POSITIVE_INFINITY, Number.POSITIVE_INFINITY],
    max: [Number.NEGATIVE_INFINITY, Number.NEGATIVE_INFINITY, Number.NEGATIVE_INFINITY],
    horizontal: newSurfaceBounds(),
    side: newSurfaceBounds(),
    trans: newSurfaceBounds(),
  };
}

function mergeSurfaceBounds(target, source) {
  target.count += source.count;
  target.area += source.area || 0;
  if (source.count) {
    includePoint(target, source.min);
    includePoint(target, source.max);
  }
  for (let index = 0; index < (source.inclinationHistogram || []).length; index++) {
    const value = source.inclinationHistogram[index] || 0;
    if (!value) continue;
    target.inclinationHistogram[index] = (target.inclinationHistogram[index] || 0) + value;
  }
  for (let index = 0; index < (source.headingHistogram || []).length; index++) {
    const value = source.headingHistogram[index] || 0;
    if (!value) continue;
    target.headingHistogram[index] = (target.headingHistogram[index] || 0) + value;
  }
}

function mergeBounds(target, source) {
  target.count += source.count;
  target.area += source.area || 0;
  if (source.count) {
    includePoint(target, source.min);
    includePoint(target, source.max);
  }
  mergeSurfaceBounds(target.horizontal, source.horizontal || newSurfaceBounds());
  mergeSurfaceBounds(target.side, source.side || newSurfaceBounds());
  mergeSurfaceBounds(target.trans, source.trans || newSurfaceBounds());
}

function readI64(buffer, offset) {
  return Number(buffer.readBigInt64LE(offset));
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
  const length = Math.hypot(normal[0], normal[1], normal[2]);
  const safeLength = length || 1;
  const nx = Math.abs(normal[0]) / safeLength;
  const ny = Math.abs(normal[1]) / safeLength;
  const nz = Math.abs(normal[2]) / safeLength;
  const horizontalNormal = Math.hypot(nx, nz);
  return {
    area: length / 2,
    nx,
    ny,
    nz,
    inclinationDeg: Math.atan2(ny, Math.max(horizontalNormal, 0.000001)) * 180 / Math.PI,
    headingAngleDeg: Math.atan2(nz, Math.max(nx, 0.000001)) * 180 / Math.PI,
  };
}

function addInclinationSample(bounds, angleDeg, area) {
  if (!Number.isFinite(angleDeg) || !Number.isFinite(area) || area <= 0) return;
  const bucket = Math.max(0, Math.min(180, Math.round(angleDeg * 2)));
  bounds.inclinationHistogram[bucket] = (bounds.inclinationHistogram[bucket] || 0) + area;
}

function addHeadingSample(bounds, angleDeg, area) {
  if (!Number.isFinite(angleDeg) || !Number.isFinite(area) || area <= 0) return;
  const bucket = Math.max(0, Math.min(180, Math.round(angleDeg * 2)));
  bounds.headingHistogram[bucket] = (bounds.headingHistogram[bucket] || 0) + area;
}

function addSurfaceTriangle(bounds, vertices, area, inclinationDeg = null, headingAngleDeg = null) {
  bounds.count++;
  bounds.area += area;
  for (const vertex of vertices) includePoint(bounds, vertex);
  addInclinationSample(bounds, inclinationDeg, area);
  addHeadingSample(bounds, headingAngleDeg, area);
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
      const vertices = [];
      for (let vertexIndex = 0; vertexIndex < 3; vertexIndex++) {
        const vertexOffset = (pos + tri * 3 + vertexIndex) * entrySize;
        const vertex = [
          data.readFloatLE(vertexOffset),
          data.readFloatLE(vertexOffset + 4),
          data.readFloatLE(vertexOffset + 8),
        ];
        vertices.push(vertex);
        includePoint(bounds, vertex);
      }
      const metrics = triangleMetrics(vertices);
      bounds.area += metrics.area;
      if (metrics.ny >= 0.85) addSurfaceTriangle(bounds.horizontal, vertices, metrics.area);
      if (metrics.nx >= 0.70) {
        addSurfaceTriangle(bounds.side, vertices, metrics.area, metrics.inclinationDeg, metrics.headingAngleDeg);
      }
      if (metrics.nz >= 0.70) addSurfaceTriangle(bounds.trans, vertices, metrics.area);
    }
    groups.set(key, bounds);
    pos += vertexCount;
  }
  return groups;
}

function mergeGroups(target, source) {
  for (const [key, sourceBounds] of source) {
    const bounds = target.get(key) || newBounds();
    mergeBounds(bounds, sourceBounds);
    target.set(key, bounds);
  }
}

function parseGeometryFile(filePath) {
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
    mergeGroups(groups, parseArmorData(buffer.subarray(dataStart, dataEnd)));
  }
  return groups;
}

function buildGeometryIndex(geometryDir) {
  const byBase = new Map();
  for (const entry of fs.readdirSync(geometryDir, { withFileTypes: true })) {
    if (!entry.isFile() || !entry.name.endsWith('.geometry')) continue;
    const filePath = path.join(geometryDir, entry.name);
    byBase.set(entry.name, filePath);
  }
  return byBase;
}

function geometryFilesForModel(modelPath, geometryIndex) {
  const base = path.basename(modelPath, path.extname(modelPath));
  const direct = geometryIndex.get(`${base}.geometry`);
  const splitFiles = [...geometryIndex]
    .filter(([name]) => name.startsWith(`${base}_`) && name.endsWith('.geometry'))
    .map(([, filePath]) => filePath);
  return direct ? [direct, ...splitFiles] : splitFiles;
}

const geometryCache = new Map();
function geometryGroupsForModel(modelPath, geometryIndex) {
  const files = geometryFilesForModel(modelPath, geometryIndex);
  if (!files.length) return null;
  const cacheKey = files.join('|');
  if (geometryCache.has(cacheKey)) return geometryCache.get(cacheKey);
  const groups = new Map();
  for (const filePath of files) mergeGroups(groups, parseGeometryFile(filePath));
  geometryCache.set(cacheKey, groups);
  return groups;
}

function isAboveWaterSide(bounds) {
  return bounds && bounds.count > 0 && bounds.min[1] >= 0.05 && bounds.max[1] > 0.10;
}

function hasVisibleAboveWaterPart(bounds) {
  return bounds && bounds.count > 0 && bounds.max[1] >= 0.05;
}

function hasNearWaterlineBeltPart(bounds) {
  return bounds && bounds.count > 0 && bounds.max[1] >= -0.05;
}

function hasVisibleHorizontalDeck(bounds) {
  return bounds?.horizontal?.count > 0 && bounds.horizontal.max[1] > 0.10;
}

function sideSurface(entry) {
  return entry.bounds?.side?.count ? entry.bounds.side : null;
}

function sideOrFullBounds(entry) {
  return sideSurface(entry) || (entry.bounds?.count ? entry.bounds : null);
}

function sideLength(entry) {
  const side = sideSurface(entry);
  return side ? side.max[2] - side.min[2] : 0;
}

function sideWidth(entry) {
  const side = sideSurface(entry);
  return side ? side.max[0] - side.min[0] : 0;
}

function sideTransArea(entry) {
  return entry.bounds?.trans?.area || 0;
}

function isCapitalKey(shipKey) {
  return /^P[A-Z]SB/.test(shipKey);
}

function isCruiserKey(shipKey) {
  return /^P[A-Z]SC/.test(shipKey);
}

function isCentralBeltMaterial(materialName) {
  const bowOrStern = isBowMaterial(materialName) || isSternMaterial(materialName);
  return !bowOrStern &&
    /Belt/.test(materialName) &&
    !/Cit|OCit|Tur|Art|Bridge|Funnel|Kdp|Rudder|Bulge|Bottom|SS_|SSC|SideSS|Deck|Trans|Inclin/.test(materialName);
}

function isCentralShellSideMaterial(materialName) {
  const bowOrStern = isBowMaterial(materialName) || isSternMaterial(materialName);
  return !bowOrStern &&
    /ConstrSide|SSC_ConstrSide/.test(materialName) &&
    !/Cit|OCit|Tur|Art|Bridge|Funnel|Kdp|Rudder|Bulge|Bottom|SS_|SideSS|Deck|Trans|Inclin/.test(materialName);
}

function hasLongitudinalSideSurface(entry) {
  const side = sideSurface(entry);
  if (!side || side.max[1] <= 0.10) return false;
  if (side.area <= 0) return false;
  return sideTransArea(entry) <= side.area * 0.70;
}

function isVisibleBeltLayer(entry) {
  if (!isCentralBeltMaterial(entry.materialName)) return false;
  if (!hasLongitudinalSideSurface(entry)) return false;
  const side = sideSurface(entry);
  if (entry.thickness <= 75) return true;
  return side.min[1] >= 0.005;
}

function isBroadSideLayer(entry, maxArea, maxLength, maxWidth) {
  const side = sideSurface(entry);
  if (!side) return false;
  const length = sideLength(entry);
  const width = sideWidth(entry);
  return side.area >= maxArea * 0.12 &&
    length >= maxLength * 0.35 &&
    width >= maxWidth * 0.45;
}

function filterBroadSideLayers(entries) {
  if (!entries.length) return [];
  const maxArea = Math.max(...entries.map((entry) => sideSurface(entry)?.area || 0));
  const maxLength = Math.max(...entries.map(sideLength));
  const maxWidth = Math.max(...entries.map(sideWidth));
  return entries.filter((entry) => isBroadSideLayer(entry, maxArea, maxLength, maxWidth));
}

function sideValues(entries) {
  return primaryVisible(entries.map((entry) => entry.thickness));
}

function armorEntriesFromHull(hull, materialNames, geometryIndex) {
  const geometryGroups = geometryGroupsForModel(hull.model, geometryIndex);
  if (!geometryGroups) return null;
  const entries = [];
  for (const [rawKey, thickness] of Object.entries(hull.armor || {})) {
    const encoded = Number(rawKey);
    const materialId = encoded % 65536;
    const layerIndex = Math.floor(encoded / 65536);
    const materialName = materialNames[materialId] || `unknown_${materialId}`;
    if (Number(thickness) <= 0) continue;
    const bounds = geometryGroups.get(`${materialId}:${layerIndex}`);
    entries.push({
      materialId,
      layerIndex,
      materialName,
      thickness: Number(thickness),
      bounds,
    });
  }
  return entries;
}

function fullHullArmorValues(hull) {
  return sortUnique(Object.values(hull.armor || {})
    .map(Number)
    .filter((value) => Number.isFinite(value) && value > 0));
}

function submarineArmorFromHull(hull) {
  const values = fullHullArmorValues(hull);
  return {
    bow: values,
    stern: values,
    deck: values,
    side: values,
    mainBelt: {
      values: [],
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
    extendedBelt: {
      present: false,
      values: [],
      bow: [],
      stern: [],
    },
  };
}

function sideValuesFromEntries(entries, shipKey) {
  const beltLayers = filterBroadSideLayers(entries.filter(isVisibleBeltLayer));
  const shellLayers = filterBroadSideLayers(entries.filter((entry) => (
    isCentralShellSideMaterial(entry.materialName) &&
    hasLongitudinalSideSurface(entry)
  )));

  if (beltLayers.length) {
    if (isCapitalKey(shipKey) || isCarrierKey(shipKey)) return sideValues(beltLayers);
    if (isCruiserKey(shipKey)) {
      const sscShell = shellLayers.filter((entry) => /^SSC_ConstrSide/.test(entry.materialName));
      return sideValues([...beltLayers, ...sscShell]);
    }
    return sideValues(beltLayers);
  }

  if (shellLayers.length) {
    if (isCarrierKey(shipKey)) return [maxValue(sideValues(shellLayers))];
    return sideValues(shellLayers);
  }

  if (isCarrierKey(shipKey)) {
    const values = entries
      .filter((entry) => isCarrierSideCandidate(entry.materialName) && hasVisibleAboveWaterPart(entry.bounds))
      .map((entry) => entry.thickness);
    return selectPrimary(values);
  }

  return [];
}

function bowSternValuesFromEntries(entries, side) {
  const isTarget = side === 'bow' ? isBowMaterial : isSternMaterial;
  const values = entries
    .filter((entry) => (
      isTarget(entry.materialName) &&
      isBowSternPlatingCandidate(entry.materialName) &&
      hasVisibleAboveWaterPart(entry.bounds)
    ))
    .map((entry) => entry.thickness);
  return primaryVisible(values);
}

function deckValuesFromEntries(entries, shipKey) {
  let candidates = entries.filter((entry) => (
    (isCarrierKey(shipKey) ? isCarrierDeckCandidate(entry.materialName) : isDeckCandidate(entry.materialName)) &&
    hasVisibleHorizontalDeck(entry.bounds)
  ));
  if (isCarrierKey(shipKey)) {
    const flightDeckCandidates = candidates.filter((entry) => /Fdck/.test(entry.materialName));
    if (flightDeckCandidates.length) candidates = flightDeckCandidates;
  }
  if (!candidates.length) return [];

  if (!isCarrierKey(shipKey) && candidates.length > 1) {
    const metrics = candidates.map((entry) => {
      const width = entry.bounds.horizontal.max[0] - entry.bounds.horizontal.min[0];
      const length = entry.bounds.horizontal.max[2] - entry.bounds.horizontal.min[2];
      return { entry, width, area: width * length };
    });
    const maxWidth = Math.max(...metrics.map((item) => item.width));
    const maxArea = Math.max(...metrics.map((item) => item.area));
    const broadCandidates = metrics
      .filter((item) => item.width >= maxWidth * 0.50 && item.area >= maxArea * 0.20)
      .map((item) => item.entry);
    if (broadCandidates.length) candidates = broadCandidates;
  }

  const topY = Math.max(...candidates.map((entry) => entry.bounds.horizontal.max[1]));
  const topTolerance = isCarrierKey(shipKey) ? 0.005 : 0.025;
  let topDeckCandidates = candidates
    .filter((entry) => Math.abs(entry.bounds.horizontal.max[1] - topY) <= topTolerance);
  if (!isCarrierKey(shipKey) && topDeckCandidates.length > 1) {
    const metrics = topDeckCandidates.map((entry) => {
      const width = entry.bounds.horizontal.max[0] - entry.bounds.horizontal.min[0];
      const length = entry.bounds.horizontal.max[2] - entry.bounds.horizontal.min[2];
      return { entry, width, area: width * length };
    });
    const maxWidth = Math.max(...metrics.map((item) => item.width));
    const maxArea = Math.max(...metrics.map((item) => item.area));
    const broadCandidates = metrics
      .filter((item) => item.width >= maxWidth * 0.55 && item.area >= maxArea * 0.20)
      .map((item) => item.entry);
    if (broadCandidates.length) {
      const broadMinThickness = Math.min(...broadCandidates.map((entry) => entry.thickness));
      topDeckCandidates = topDeckCandidates.filter((entry) => (
        broadCandidates.includes(entry) || entry.thickness <= broadMinThickness
      ));
    }
  }
  const topDeckValues = topDeckCandidates
    .map((entry) => entry.thickness);
  return primaryVisible(topDeckValues);
}

function beltValuesFromEntries(entries, side) {
  const isTarget = side === 'bow' ? isBowMaterial : isSternMaterial;
  return primaryVisible(entries
    .filter((entry) => (
      isTarget(entry.materialName) &&
      /Belt/.test(entry.materialName) &&
      !/Cit|OCit|Tur|Art|Bridge|Funnel|Kdp|Rudder|Bulge|Bottom|SS_|SSC|SideSS/.test(entry.materialName) &&
      hasNearWaterlineBeltPart(entry.bounds)
    ))
    .map((entry) => entry.thickness));
}

function rangesTouchOrOverlap(left, right, axis, tolerance) {
  return Math.min(left.max[axis], right.max[axis]) >= Math.max(left.min[axis], right.min[axis]) - tolerance;
}

function isConnectedToMainBelt(candidate, mainBeltEntries, side) {
  const candidateBounds = sideOrFullBounds(candidate);
  if (!candidateBounds) return false;

  return mainBeltEntries.some((mainBelt) => {
    const mainBounds = sideOrFullBounds(mainBelt);
    if (!mainBounds) return false;
    if (!rangesTouchOrOverlap(candidateBounds, mainBounds, 0, 0.05)) return false;
    if (!rangesTouchOrOverlap(candidateBounds, mainBounds, 1, 0.02)) return false;

    const longitudinalGap = side === 'bow'
      ? candidateBounds.min[2] - mainBounds.max[2]
      : mainBounds.min[2] - candidateBounds.max[2];
    return Math.abs(longitudinalGap) <= 0.15;
  });
}

function connectedBeltValuesFromEntries(entries, side) {
  const isTarget = side === 'bow' ? isBowMaterial : isSternMaterial;
  const mainBeltEntries = entries.filter((entry) => (
    isCentralBeltMaterial(entry.materialName) &&
    sideOrFullBounds(entry)
  ));
  if (!mainBeltEntries.length) return [];

  return primaryVisible(entries
    .filter((entry) => (
      isTarget(entry.materialName) &&
      /Belt/.test(entry.materialName) &&
      !/Cit|OCit|Tur|Art|Bridge|Funnel|Kdp|Rudder|Bulge|Bottom|SS_|SSC|SideSS/.test(entry.materialName) &&
      hasNearWaterlineBeltPart(entry.bounds) &&
      isConnectedToMainBelt(entry, mainBeltEntries, side)
    ))
    .map((entry) => entry.thickness));
}

function extendedBeltFromEntries(entries, bowValues, sternValues) {
  const bow = beltValuesFromEntries(entries, 'bow');
  const stern = beltValuesFromEntries(entries, 'stern');
  return {
    present: bow.length > 0 || stern.length > 0,
    values: sortUnique([...bow, ...stern]),
    bow,
    stern,
  };
}

function isPrimaryMainBeltMaterial(materialName) {
  const bowOrStern = isBowMaterial(materialName) || isSternMaterial(materialName);
  return !bowOrStern &&
    /(^|_)Cit_Belt$|(^|_)OCit_Belt$|Dual_Cit_Cas_Belt|Dual_Cit_SSC_Belt|SideCit|^Belt$/.test(materialName) &&
    !/Bow|St_|St$|Trans|Deck|Bottom|Bulge|Tur|Art|Bridge|Funnel|Kdp|Rudder|SS_|SSC_|SideSS|Inclin/.test(materialName);
}

function isFallbackMainBeltMaterial(materialName) {
  const bowOrStern = isBowMaterial(materialName) || isSternMaterial(materialName);
  return !bowOrStern &&
    /Belt/.test(materialName) &&
    !/Bow|St_|St$|Trans|Deck|Bottom|Bulge|Tur|Art|Bridge|Funnel|Kdp|Rudder|SS_|SideSS|Inclin/.test(materialName);
}

function hasMainBeltSurface(entry) {
  const side = sideSurface(entry);
  if (!side || side.area <= 0) return false;
  if (sideTransArea(entry) > side.area * 0.35) return false;
  return side.max[1] >= -0.85;
}

function weightedPercentileFromHistogram(histogram, percentile) {
  const total = (histogram || []).reduce((sum, area) => sum + (area || 0), 0);
  if (total <= 0) return null;
  const threshold = total * percentile;
  let running = 0;
  for (let index = 0; index < histogram.length; index++) {
    running += histogram[index] || 0;
    if (running >= threshold) return index / 2;
  }
  return (histogram.length - 1) / 2;
}

function inclinationRangeFromEntries(entries) {
  const histogram = [];
  for (const entry of entries) {
    const side = sideSurface(entry);
    for (let index = 0; index < (side?.inclinationHistogram || []).length; index++) {
      const area = side.inclinationHistogram[index] || 0;
      if (!area) continue;
      histogram[index] = (histogram[index] || 0) + area;
    }
  }

  const min = weightedPercentileFromHistogram(histogram, 0.10);
  const max = weightedPercentileFromHistogram(histogram, 0.90);
  if (min == null || max == null) {
    return { min: 0, max: 0, estimated: true };
  }

  return {
    min: Math.round(Math.min(min, max) * 10) / 10,
    max: Math.round(Math.max(min, max) * 10) / 10,
    estimated: false,
  };
}

function headingAngleRangeFromEntries(entries) {
  const histogram = [];
  for (const entry of entries) {
    const side = sideSurface(entry);
    for (let index = 0; index < (side?.headingHistogram || []).length; index++) {
      const area = side.headingHistogram[index] || 0;
      if (!area) continue;
      histogram[index] = (histogram[index] || 0) + area;
    }
  }

  const min = weightedPercentileFromHistogram(histogram, 0.10);
  const max = weightedPercentileFromHistogram(histogram, 0.90);
  if (min == null || max == null) {
    return { min: 0, max: 0, estimated: true };
  }

  return {
    min: Math.round(Math.min(min, max) * 10) / 10,
    max: Math.round(Math.max(min, max) * 10) / 10,
    estimated: false,
  };
}

function mainBeltFromEntries(entries, shipKey) {
  if (isSubmarineKey(shipKey)) {
    return {
      values: [],
      inclinationDeg: { min: 0, max: 0, estimated: true },
      headingAngleDeg: { min: 0, max: 0, estimated: true },
    };
  }

  let candidates = filterBroadSideLayers(entries.filter((entry) => (
    isPrimaryMainBeltMaterial(entry.materialName) &&
    hasMainBeltSurface(entry)
  )));
  if (!candidates.length) {
    candidates = filterBroadSideLayers(entries.filter((entry) => (
      isFallbackMainBeltMaterial(entry.materialName) &&
      hasMainBeltSurface(entry)
    )));
  }
  if (!candidates.length) {
    return {
      values: [],
      inclinationDeg: { min: 0, max: 0, estimated: true },
      headingAngleDeg: { min: 0, max: 0, estimated: true },
    };
  }

  const strongest = Math.max(...candidates.map((entry) => entry.thickness));
  const selected = candidates.filter((entry) => entry.thickness === strongest);
  return {
    values: sideValues(selected),
    inclinationDeg: inclinationRangeFromEntries(selected),
    headingAngleDeg: headingAngleRangeFromEntries(selected),
  };
}

function armorValuesFromHull(shipKey, hull, materialNames, geometryIndex) {
  if (isSubmarineKey(shipKey)) return submarineArmorFromHull(hull);
  const entries = armorEntriesFromHull(hull, materialNames, geometryIndex);
  if (!entries) return null;
  const bow = bowSternValuesFromEntries(entries, 'bow');
  const stern = bowSternValuesFromEntries(entries, 'stern');
  return {
    bow,
    stern,
    deck: deckValuesFromEntries(entries, shipKey),
    side: sideValuesFromEntries(entries, shipKey),
    extendedBelt: extendedBeltFromEntries(entries, bow, stern),
    mainBelt: mainBeltFromEntries(entries, shipKey),
  };
}

function sideValuesFromHull(hull, materialNames, geometryIndex) {
  const entries = armorEntriesFromHull(hull, materialNames, geometryIndex);
  if (!entries) return null;
  const values = [];
  for (const entry of entries) {
    if (!isSideCandidate(entry.materialName)) continue;
    if (isAboveWaterSide(entry.bounds)) values.push(entry.thickness);
  }
  return selectPrimary(values);
}

function pythonLiteral(value, depth = 0) {
  const indent = '  '.repeat(depth);
  const nextIndent = '  '.repeat(depth + 1);
  if (value === null) return 'None';
  if (typeof value === 'boolean') return value ? 'True' : 'False';
  if (typeof value === 'number') return String(value);
  if (typeof value === 'string') return JSON.stringify(value);
  if (Array.isArray(value)) {
    if (!value.length) return '[]';
    return `[\n${value.map((item) => `${nextIndent}${pythonLiteral(item, depth + 1)}`).join(',\n')}\n${indent}]`;
  }
  if (typeof value === 'object') {
    const entries = Object.entries(value);
    if (!entries.length) return '{}';
    return `{\n${entries.map(([key, item]) => `${nextIndent}${pythonLiteral(key)}: ${pythonLiteral(item, depth + 1)}`).join(',\n')}\n${indent}}`;
  }
  throw new Error(`Unsupported Python literal type: ${typeof value}`);
}

function writePythonDatabase(database, outPath) {
  const pyOutPath = outPath.replace(/\.[^.]*$/, '.py');
  const pyText = `# -*- coding: utf-8 -*-\n# Generated from armor_overmatch.json. WoWS ModsAPI blocks the json module.\nDATABASE = ${pythonLiteral(database)}\n`;
  fs.writeFileSync(pyOutPath, pyText, 'utf8');
}

function intersectExisting(candidateValues, currentValues) {
  const currentSet = new Set(currentValues);
  return sortUnique(candidateValues.filter((value) => currentSet.has(value)));
}

function sameInclination(left = {}, right = {}) {
  return Number(left.min || 0) === Number(right.min || 0) &&
    Number(left.max || 0) === Number(right.max || 0) &&
    Boolean(left.estimated) === Boolean(right.estimated);
}

function sameMainBelt(left = {}, right = {}) {
  return sameValues(sortUnique(left.values || []), sortUnique(right.values || [])) &&
    sameInclination(left.inclinationDeg || {}, right.inclinationDeg || {}) &&
    sameInclination(left.headingAngleDeg || {}, right.headingAngleDeg || {});
}

async function refineDatabase(db, gameParamsPath, materialNames, geometryIndex, options = {}) {
  const shipKeys = new Set(Object.keys(db.ships || {}));
  const stream = fs.createReadStream(gameParamsPath, { encoding: 'utf8' });
  const rl = readline.createInterface({ input: stream, crlfDelay: Infinity });
  let capturing = false;
  let depth = 0;
  let entryName = null;
  let lines = [];
  let changed = 0;
  let changedBowStern = 0;
  let changedDeck = 0;
  let changedExtendedBelt = 0;
  let changedMainBelt = 0;
  let inspected = 0;
  let missingGeometry = 0;
  let protectedDestroyers = 0;
  let carrierSideChanged = 0;

  for await (const line of rl) {
    if (!capturing) {
      const match = line.match(/^  "([^"]+)": \{/);
      if (match && shipKeys.has(match[1])) {
        capturing = true;
        depth = jsonDepthDelta(line);
        entryName = match[1];
        lines = [line];
      }
      continue;
    }

    lines.push(line);
    depth += jsonDepthDelta(line);
    if (depth !== 0) continue;

    const fragment = lines.join('\n').replace(/,\s*$/, '');
    const ship = JSON.parse(`{${fragment}}`)[entryName];
    const hulls = collectHullObjects(ship);
    const selectedHull = hulls.at(-1);
    const dbShip = db.ships[entryName];
    if (selectedHull && dbShip?.armor) {
      inspected++;
      const geometryArmor = armorValuesFromHull(entryName, selectedHull, materialNames, geometryIndex);
      if (geometryArmor === null) {
        missingGeometry++;
        if (!options.mainBeltOnly && !isSubmarineKey(entryName) && dbShip?.armor?.extendedBowSternBelt?.present) {
          dbShip.armor.extendedBowSternBelt = {
            present: false,
            values: [],
            bow: [],
            stern: [],
          };
          changedExtendedBelt++;
        }
      } else {
        const armor = dbShip.armor;
        const bowStern = armor.bowStern || {};
        const isSubmarine = isSubmarineKey(entryName);

        if (options.updateMainBelt && geometryArmor.mainBelt?.values?.length) {
          const currentMainBelt = armor.mainBelt || {};
          if (!sameMainBelt(currentMainBelt, geometryArmor.mainBelt)) {
            armor.mainBelt = geometryArmor.mainBelt;
            changedMainBelt++;
          }
        }

        if (options.mainBeltOnly) {
          capturing = false;
          entryName = null;
          lines = [];
          continue;
        }

        const currentBow = sortUnique(bowStern.bow || []);
        if (isSubmarine && geometryArmor.bow.length) {
          if (!sameValues(currentBow, geometryArmor.bow)) {
            bowStern.bow = geometryArmor.bow;
            changedBowStern++;
          }
        } else if (geometryArmor.bow.length && currentBow.length) {
          const nextBow = intersectExisting(geometryArmor.bow, currentBow);
          if (nextBow.length && !sameValues(currentBow, nextBow)) {
            bowStern.bow = nextBow;
            changedBowStern++;
          }
        }
        const currentStern = sortUnique(bowStern.stern || []);
        if (isSubmarine && geometryArmor.stern.length) {
          if (!sameValues(currentStern, geometryArmor.stern)) {
            bowStern.stern = geometryArmor.stern;
            changedBowStern++;
          }
        } else if (geometryArmor.stern.length && currentStern.length) {
          const nextStern = intersectExisting(geometryArmor.stern, currentStern);
          if (nextStern.length && !sameValues(currentStern, nextStern)) {
            bowStern.stern = nextStern;
            changedBowStern++;
          }
        }
        armor.bowStern = bowStern;

        if (options.updateDeck && geometryArmor.deck.length) {
          const deck = armor.deck || {};
          const currentDeck = sortUnique(deck.values || []);
          if (!sameValues(currentDeck, geometryArmor.deck)) {
            deck.values = geometryArmor.deck;
            armor.deck = deck;
            changedDeck++;
          }
        }

        const belt = armor.extendedBowSternBelt || {};
        const nextBelt = geometryArmor.extendedBelt;
        const nextExistingBelt = {
          present: false,
          values: [],
          bow: [],
          stern: [],
        };
        const currentBelt = {
          present: Boolean(belt.present),
          values: sortUnique(belt.values || []),
          bow: sortUnique(belt.bow || []),
          stern: sortUnique(belt.stern || []),
        };
        nextExistingBelt.bow = intersectExisting(nextBelt.bow, currentBelt.bow);
        nextExistingBelt.stern = intersectExisting(nextBelt.stern, currentBelt.stern);
        nextExistingBelt.values = sortUnique([...nextExistingBelt.bow, ...nextExistingBelt.stern]);
        nextExistingBelt.present = nextExistingBelt.values.length > 0;
        if (
          currentBelt.present !== nextExistingBelt.present ||
          !sameValues(currentBelt.values, nextExistingBelt.values) ||
          !sameValues(currentBelt.bow, nextExistingBelt.bow) ||
          !sameValues(currentBelt.stern, nextExistingBelt.stern)
        ) {
          belt.present = nextExistingBelt.present;
          belt.values = nextExistingBelt.values;
          belt.bow = nextExistingBelt.bow;
          belt.stern = nextExistingBelt.stern;
          armor.extendedBowSternBelt = belt;
          changedExtendedBelt++;
        }

        if (!armor.side) armor.side = {};
        const geometrySide = geometryArmor.side;
        if (!geometrySide.length && !isCarrierKey(entryName)) {
          capturing = false;
          entryName = null;
          lines = [];
          continue;
        }
        const currentSide = sortUnique(dbShip.armor.side.values || []);
        const nextSideValues = [...geometrySide];
        if (isDestroyerKey(entryName)) {
          const strongestSide = maxValue(currentSide);
          if (strongestSide && !nextSideValues.includes(strongestSide)) {
            nextSideValues.push(strongestSide);
            protectedDestroyers++;
          }
        }
        const nextSide = sortUnique(nextSideValues);
        if (!sameValues(currentSide, nextSide)) {
          if (nextSide.length) {
            dbShip.armor.side.values = nextSide;
            changed++;
            if (isCarrierKey(entryName)) carrierSideChanged++;
          }
        }
      }
    }

    capturing = false;
    entryName = null;
    lines = [];
  }

  return {
    changed,
    changedBowStern,
    changedDeck,
    changedExtendedBelt,
    changedMainBelt,
    inspected,
    missingGeometry,
    protectedDestroyers,
    carrierSideChanged,
  };
}

const args = parseArgs(process.argv.slice(2));
const dbPath = args.db || path.join(projectRoot, 'src', 'res_mods', 'PnFMods', 'APOvermatchAssistant', 'data', 'armor_overmatch.json');
const gameParamsPath = args['game-params'] || 'C:\\tmp\\GameParams_ASIA.json';
const geometryDir = args['geometry-dir'] || path.join(projectRoot, 'build', 'scratch', 'ship_geometry_flat');

const db = readJsonFile(dbPath);
const materialNames = loadMaterialNames();
const geometryIndex = buildGeometryIndex(geometryDir);
const result = await refineDatabase(db, gameParamsPath, materialNames, geometryIndex, {
  updateDeck: args['no-update-deck'] ? false : true,
  updateMainBelt: args['no-update-main-belt'] ? false : true,
  mainBeltOnly: Boolean(args['main-belt-only']),
});

if (db.meta) {
  const note = 'Armor groups are refined from armor geometry where available: deck uses broad outer horizontal deck surfaces (carriers use the highest flight deck), side uses longitudinal side surfaces from visible side or casemate armor while excluding transverse bulkheads, local superstructure/turret faces, and lower belt extensions, mainBelt is extracted from central citadel belt geometry and stores both vertical inclination and horizontal heading-relative angle ranges, submarines use all positive final-hull armor values for hull armor because positional geometry is not useful there, bow/stern values conservatively remove values not visible in end plating positions, extended belt separately keeps near-waterline Bow_Belt and St_Belt plates as fore and aft armor belt groups, and destroyers preserve their strongest original side value because their thickest main hull plating counts as outer side armor.';
  db.meta.notes = db.meta.notes && !db.meta.notes.includes(note)
    ? `${note} ${db.meta.notes}`
    : (db.meta.notes || note);
}

fs.writeFileSync(dbPath, `${JSON.stringify(db, null, 2)}\n`, 'utf8');
writePythonDatabase(db, dbPath);
console.log(`Geometry side refinement inspected ${result.inspected} ships.`);
console.log(`Geometry side refinement changed ${result.changed} ships.`);
console.log(`Geometry bow/stern refinement changed ${result.changedBowStern} field(s).`);
console.log(`Geometry deck refinement changed ${result.changedDeck} ship(s).`);
console.log(`Geometry extended belt refinement changed ${result.changedExtendedBelt} ship(s).`);
console.log(`Geometry main belt extraction changed ${result.changedMainBelt} ship(s).`);
console.log(`Geometry side refinement missing geometry for ${result.missingGeometry} ships.`);
console.log(`Geometry side refinement protected ${result.protectedDestroyers} destroyer side value(s).`);
console.log(`Geometry side refinement changed ${result.carrierSideChanged} carrier side value(s).`);
