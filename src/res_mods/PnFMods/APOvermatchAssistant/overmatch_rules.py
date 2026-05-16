# -*- coding: utf-8 -*-

from overmatch_constants import (
    AMMO_AP,
    AMMO_HE,
    AMMO_SAP,
    OVERMATCH_DIVISOR,
    STATE_NO,
    STATE_PARTIAL,
    STATE_TEXT_OVERMATCH,
    STATE_TEXT_PEN,
    STATE_UNKNOWN,
    STATE_YES,
    TXT_OVERMATCH_LIMIT,
    TXT_PENETRATION,
)
from overmatch_utils import as_float, format_single_mm


def record_number(record, name):
    if not record:
        return None
    return as_float(record.get(name))


def rule_limit_for_ammo(ammo_kind, caliber, ship_record):
    if ammo_kind == AMMO_AP:
        if caliber is None:
            return None
        return caliber / OVERMATCH_DIVISOR
    if ammo_kind == AMMO_HE:
        value = record_number(ship_record, 'mainGunHePenMm')
        if value is not None:
            return value
        if caliber is not None:
            return int(caliber / 6.0)
        return None
    if ammo_kind == AMMO_SAP:
        return record_number(ship_record, 'mainGunSapPenMm')
    return None


def weapon_text(ammo_kind, caliber, limit):
    if ammo_kind == AMMO_AP:
        if caliber is None:
            return u'AP ? mm'
        return u'AP {} ({} {})'.format(
            format_single_mm(caliber),
            TXT_OVERMATCH_LIMIT,
            format_single_mm(limit),
        )
    if ammo_kind == AMMO_HE:
        return u'HE {} {}'.format(format_single_mm(limit), TXT_PENETRATION)
    if ammo_kind == AMMO_SAP:
        return u'SAP {} {}'.format(format_single_mm(limit), TXT_PENETRATION)
    return u'?'


def state_text_for_ammo(ammo_kind):
    if ammo_kind == AMMO_AP:
        return STATE_TEXT_OVERMATCH
    return STATE_TEXT_PEN


def flatten_values(group):
    values = []
    if not group:
        return values
    if isinstance(group, list):
        source = group
    elif isinstance(group, dict):
        source = []
        for key in ('values', 'bow', 'stern', 'fore', 'aft', 'main'):
            item = group.get(key)
            if isinstance(item, list):
                source += item
            elif item is not None:
                source.append(item)
    else:
        source = [group]

    for item in source:
        mm = as_float(item)
        if mm is not None and mm > 0 and mm not in values:
            values.append(mm)
    values.sort()
    return values


def state_for_limit(values, limit_mm):
    if not values or limit_mm is None:
        return STATE_UNKNOWN
    hits = [limit_mm >= value for value in values]
    if all(hits):
        return STATE_YES
    if any(hits):
        return STATE_PARTIAL
    return STATE_NO


def merge_states(states):
    filtered = [state for state in states if state != STATE_UNKNOWN]
    if not filtered:
        return STATE_UNKNOWN
    if all(state == STATE_YES for state in filtered):
        return STATE_YES
    if all(state == STATE_NO for state in filtered):
        return STATE_NO
    return STATE_PARTIAL
