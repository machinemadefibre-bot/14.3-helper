# -*- coding: utf-8 -*-

from overmatch_constants import (
    DEFAULT_PAYLOAD,
    STATE_COLOR,
    STATE_YES,
    TXT_BELT,
    TXT_BOW,
    TXT_BOW_STERN,
    TXT_DECK,
    TXT_FRONT,
    TXT_NO_BELT,
    TXT_REAR,
    TXT_SIDE,
    TXT_STERN,
)
from overmatch_rules import (
    flatten_values,
    merge_states,
    state_for_limit,
    state_text_for_ammo,
    weapon_text,
)
from overmatch_utils import format_mm


def default_payload():
    return dict(DEFAULT_PAYLOAD)


class OvermatchPayloadBuilder(object):
    def build_target_payload(self, target_name, target_record, ammo_kind, caliber, limit):
        payload = default_payload()
        payload['visible'] = True
        payload['targetName'] = target_name
        payload['weaponText'] = weapon_text(ammo_kind, caliber, limit)
        payload['caliberText'] = payload['weaponText']

        armor = target_record.get('armor', {}) if target_record else {}
        state_text = state_text_for_ammo(ammo_kind)
        self._apply_bow_stern(payload, armor.get('bowStern'), limit, state_text)
        self._apply_simple(payload, 'deck', TXT_DECK, armor.get('deck'), limit, state_text)
        self._apply_simple(payload, 'side', TXT_SIDE, armor.get('side'), limit, state_text)
        self._apply_belt(payload, armor.get('extendedBowSternBelt'), limit, state_text)
        return payload

    def _apply_bow_stern(self, payload, group, limit, state_text):
        if isinstance(group, dict) and ('bow' in group or 'stern' in group):
            bow = flatten_values(group.get('bow') or group.get('fore') or group.get('values'))
            stern = flatten_values(group.get('stern') or group.get('aft') or group.get('values'))
            bow_state = state_for_limit(bow, limit)
            stern_state = state_for_limit(stern, limit)
            state = merge_states([bow_state, stern_state])
            payload['bowSternText'] = u'{}: {} {} / {} {} ({} / {})'.format(
                TXT_BOW_STERN,
                TXT_BOW,
                state_text[bow_state],
                TXT_STERN,
                state_text[stern_state],
                format_mm(bow),
                format_mm(stern),
            )
            payload['bowSternColor'] = STATE_COLOR[state]
            return

        values = flatten_values(group)
        state = state_for_limit(values, limit)
        payload['bowSternText'] = u'{}: {} ({})'.format(TXT_BOW_STERN, state_text[state], format_mm(values))
        payload['bowSternColor'] = STATE_COLOR[state]

    def _apply_simple(self, payload, key, label, group, limit, state_text):
        values = flatten_values(group)
        state = state_for_limit(values, limit)
        payload[key + 'Text'] = u'{}: {} ({})'.format(label, state_text[state], format_mm(values))
        payload[key + 'Color'] = STATE_COLOR[state]

    def _apply_belt(self, payload, group, limit, state_text):
        present = True
        if not group:
            present = False
        elif isinstance(group, dict) and 'present' in group:
            present = bool(group.get('present'))

        if not present:
            payload['beltText'] = u'{}\uff1a{}\uff1a{}  {}\uff1a{}'.format(
                TXT_BELT,
                TXT_FRONT,
                TXT_NO_BELT,
                TXT_REAR,
                TXT_NO_BELT,
            )
            payload['beltColor'] = STATE_COLOR[STATE_YES]
            return

        bow = flatten_values(group.get('bow') or group.get('fore')) if isinstance(group, dict) else []
        stern = flatten_values(group.get('stern') or group.get('aft')) if isinstance(group, dict) else []
        if not bow and not stern:
            bow = flatten_values(group)
        bow_state = state_for_limit(bow, limit) if bow else STATE_YES
        stern_state = state_for_limit(stern, limit) if stern else STATE_YES
        state = merge_states([bow_state, stern_state])
        bow_text = state_text[bow_state] if bow else TXT_NO_BELT
        stern_text = state_text[stern_state] if stern else TXT_NO_BELT
        payload['beltText'] = u'{}\uff1a{}\uff1a{}  {}\uff1a{}'.format(
            TXT_BELT,
            TXT_FRONT,
            bow_text,
            TXT_REAR,
            stern_text,
        )
        payload['beltColor'] = STATE_COLOR[state]
