# -*- coding: utf-8 -*-

try:
    unicode
except NameError:
    unicode = str


def safe_getattr(obj, name, default=None):
    try:
        if obj is None:
            return default
        if isinstance(obj, dict):
            return obj.get(name, default)
        return getattr(obj, name, default)
    except Exception:
        return default


def get_path(obj, path):
    cur = obj
    for part in path:
        cur = safe_getattr(cur, part)
        if cur is None:
            return None
    return cur


def as_float(value, default=None):
    try:
        if value is None:
            return default
        return float(value)
    except Exception:
        return default


def normal_key(value):
    try:
        return unicode(value).strip().lower()
    except Exception:
        try:
            return str(value).strip().lower()
        except Exception:
            return ''


def normalize_caliber_mm(value):
    caliber = as_float(value)
    if caliber is None or caliber <= 0:
        return None
    if caliber < 5:
        caliber *= 1000.0
    elif caliber < 80:
        caliber *= 10.0
    return round(caliber, 1)


def format_mm(values):
    clean = []
    for value in values:
        mm = as_float(value)
        if mm is not None and mm > 0 and mm not in clean:
            clean.append(mm)
    clean.sort()
    if not clean:
        return u'? mm'
    result = []
    for mm in clean:
        if abs(mm - int(mm)) < 0.01:
            result.append(u'{} mm'.format(int(mm)))
        else:
            result.append(u'{:.1f} mm'.format(mm))
    return u'/'.join(result)


def format_single_mm(value):
    mm = as_float(value)
    if mm is None or mm <= 0:
        return u'? mm'
    if abs(mm - int(mm)) < 0.01:
        return u'{} mm'.format(int(mm))
    return u'{:.1f} mm'.format(mm)
