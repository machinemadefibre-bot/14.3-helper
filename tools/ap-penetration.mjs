export const AP_RANGE_SAMPLES_KM = [0, 5, 10, 15, 20, 25, 30];

const USN_KRUPP_SCALE = 1e-7;
const DRAG_RANGE_SCALE_KM = 12.5;
const GRAVITY_MPS2 = 9.80665;

function num(value) {
  const result = Number(value);
  return Number.isFinite(result) ? result : null;
}

function round(value, digits = 1) {
  const scale = 10 ** digits;
  return Math.round(value * scale) / scale;
}

function degToRad(value) {
  return value * Math.PI / 180;
}

export function trajectoryArmorEffectiveMm(armorMm, horizontalObliquityDeg = 0, verticalObliquityDeg = 0) {
  const armor = num(armorMm);
  if (!armor) return null;
  const horizontal = Math.min(80, Math.max(0, num(horizontalObliquityDeg) ?? 0));
  const vertical = Math.min(80, Math.max(0, num(verticalObliquityDeg) ?? 0));
  const trajectoryCos = Math.cos(degToRad(horizontal)) * Math.cos(degToRad(vertical));
  return armor / Math.max(0.18, trajectoryCos);
}

export function verticalObliquityToSlopeRangeDeg(impactAngleDeg, slopeMinDeg = 0, slopeMaxDeg = slopeMinDeg) {
  const impact = Math.max(0, num(impactAngleDeg) ?? 0);
  const slopeMin = Math.max(0, num(slopeMinDeg) ?? 0);
  const slopeMax = Math.max(slopeMin, num(slopeMaxDeg) ?? slopeMin);
  const min = impact < slopeMin ? slopeMin - impact : impact > slopeMax ? impact - slopeMax : 0;
  const lowEdge = Math.abs(impact - slopeMin);
  const highEdge = Math.abs(impact - slopeMax);
  return {
    min,
    max: Math.max(lowEdge, highEdge),
  };
}

export function usnRawPenetrationMm(shell, velocityMps = shell.muzzleVelocityMps) {
  const massKg = num(shell.massKg);
  const caliberM = num(shell.caliberM);
  const krupp = num(shell.krupp);
  const velocity = num(velocityMps);
  if (!massKg || !caliberM || !krupp || !velocity) return null;
  return krupp * ((massKg * velocity * velocity) ** 0.69) * (caliberM ** -1.07) * USN_KRUPP_SCALE;
}

export function apSample(shell, rangeKm) {
  const muzzleVelocity = num(shell.muzzleVelocityMps);
  const airDrag = Math.max(0, num(shell.airDrag) ?? 0);
  const range = Math.max(0, num(rangeKm) ?? 0);
  if (!muzzleVelocity) return null;

  const velocity = muzzleVelocity * Math.exp(-(airDrag * range) / DRAG_RANGE_SCALE_KM);
  const averageVelocity = Math.max(1, (muzzleVelocity + velocity) * 0.5);
  const flightTime = (range * 1000) / averageVelocity;
  const verticalVelocity = GRAVITY_MPS2 * flightTime * 0.5;
  const impactAngleDeg = range <= 0 ? 0 : Math.atan2(verticalVelocity, Math.max(1, velocity)) * 180 / Math.PI;
  const verticalPenetrationMm = usnRawPenetrationMm(shell, velocity);
  const horizontalPenetrationMm = verticalPenetrationMm == null
    ? null
    : verticalPenetrationMm * Math.sin(impactAngleDeg * Math.PI / 180);

  return {
    rangeKm: round(range, 1),
    verticalPenetrationMm: round(verticalPenetrationMm ?? 0, 1),
    horizontalPenetrationMm: round(horizontalPenetrationMm ?? 0, 1),
    impactAngleDeg: round(impactAngleDeg, 1),
    flightTimeSec: round(flightTime, 2),
    velocityMps: round(velocity, 1),
  };
}

export function buildApBallisticTable(shell, rangesKm = AP_RANGE_SAMPLES_KM) {
  return rangesKm
    .map((rangeKm) => apSample(shell, rangeKm))
    .filter(Boolean);
}

export function normalizeApShell(raw) {
  const caliberM = num(raw.caliberM);
  const caliberMm = num(raw.caliberMm) ?? (caliberM ? caliberM * 1000 : null);
  const shell = {
    shellName: raw.shellName || raw.name || '',
    caliberMm: caliberMm ? round(caliberMm, 1) : null,
    caliberM: caliberM ?? (caliberMm ? caliberMm / 1000 : null),
    massKg: num(raw.massKg),
    muzzleVelocityMps: num(raw.muzzleVelocityMps),
    krupp: num(raw.krupp),
    airDrag: num(raw.airDrag) ?? 0,
    ricochetAtDeg: num(raw.ricochetAtDeg) ?? 45,
    alwaysRicochetAtDeg: num(raw.alwaysRicochetAtDeg) ?? 60,
    normalizationDeg: num(raw.normalizationDeg) ?? 0,
    hasCap: Boolean(raw.hasCap),
    detonatorThresholdMm: num(raw.detonatorThresholdMm),
    detonatorSec: num(raw.detonatorSec),
  };

  if (!shell.caliberMm || !shell.caliberM || !shell.massKg || !shell.muzzleVelocityMps || !shell.krupp) {
    return null;
  }

  shell.table = buildApBallisticTable(shell);
  return shell;
}

export function mainBeltVerdict(shell, target) {
  const beltMm = num(target.beltMm);
  const rangeKm = num(target.rangeKm);
  const obliquityDeg = Math.max(0, num(target.obliquityDeg) ?? 0);
  const slopeDeg = Math.max(0, num(target.slopeDeg) ?? 0);
  if (!shell || !shell.table || !shell.table.length || !beltMm || rangeKm == null) return 'unknown';

  const bucket = shell.table.reduce((best, row) => (
    Math.abs(row.rangeKm - rangeKm) < Math.abs(best.rangeKm - rangeKm) ? row : best
  ), shell.table[0]);
  const impactAngleDeg = num(bucket.impactAngleDeg) ?? 0;
  const verticalObliquity = verticalObliquityToSlopeRangeDeg(impactAngleDeg, slopeDeg, slopeDeg);
  const rawTrajectoryCos = Math.cos(degToRad(Math.min(80, obliquityDeg)))
    * Math.cos(degToRad(Math.min(80, verticalObliquity.min)));
  const alwaysRicochetAtDeg = num(shell.alwaysRicochetAtDeg) ?? 90;
  if (rawTrajectoryCos <= Math.cos(degToRad(alwaysRicochetAtDeg))) return 'no';

  const normalizedObliquity = Math.max(0, obliquityDeg - (num(shell.normalizationDeg) ?? 0));
  const effectiveBeltMm = trajectoryArmorEffectiveMm(beltMm, normalizedObliquity, verticalObliquity.min);
  const trajectoryPenetrationMm = num(bucket.trajectoryPenetrationMm) ?? bucket.verticalPenetrationMm;
  if (trajectoryPenetrationMm * 0.95 >= effectiveBeltMm) return 'yes';
  if (trajectoryPenetrationMm * 1.05 >= effectiveBeltMm) return 'partial';
  return 'no';
}
