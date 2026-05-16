# -*- coding: utf-8 -*-

import os
import sys
import types
import tempfile
import textwrap
import unittest


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
MOD_DIR = os.path.join(PROJECT_ROOT, 'src', 'res_mods', 'PnFMods', 'APOvermatchAssistant')
if MOD_DIR not in sys.path:
    sys.path.insert(0, MOD_DIR)

from overmatch_constants import (
    AMMO_AP,
    AMMO_HE,
    AMMO_SAP,
    AMMO_TORPEDO,
    COMPONENT_KEY,
    DEFAULT_PAYLOAD,
    STATE_COLOR,
    STATE_NO,
    STATE_PARTIAL,
    STATE_TEXT_OVERMATCH,
    STATE_TEXT_PEN,
    STATE_UNKNOWN,
    STATE_YES,
)
from overmatch_database import ArmorDatabase
from overmatch_payload import OvermatchPayloadBuilder, default_payload
from overmatch_rules import (
    flatten_values,
    merge_states,
    record_number,
    rule_limit_for_ammo,
    state_for_limit,
    state_text_for_ammo,
    weapon_text,
)
from overmatch_utils import (
    as_float,
    format_mm,
    format_single_mm,
    get_path,
    normal_key,
    normalize_caliber_mm,
    safe_getattr,
)

fake_events = types.ModuleType('events')
fake_events.onBattleStart = lambda handler: None
fake_events.onBattleQuit = lambda handler: None
sys.modules.setdefault('events', fake_events)

import Main


class Struct(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class OvermatchUtilsTests(unittest.TestCase):
    def test_safe_getattr_supports_objects_dicts_and_defaults(self):
        self.assertEqual(safe_getattr({'name': 'Yamato'}, 'name'), 'Yamato')
        self.assertEqual(safe_getattr(Struct(name='Yamato'), 'name'), 'Yamato')
        self.assertEqual(safe_getattr(None, 'name', 'fallback'), 'fallback')
        self.assertEqual(safe_getattr(object(), 'missing', 'fallback'), 'fallback')

    def test_get_path_stops_cleanly_on_missing_segments(self):
        data = {'shipConfig': {'artillery': {'caliber': '0.46'}}}
        self.assertEqual(get_path(data, ('shipConfig', 'artillery', 'caliber')), '0.46')
        self.assertIsNone(get_path(data, ('shipConfig', 'missing', 'caliber')))

    def test_float_and_caliber_helpers_normalize_game_units(self):
        self.assertEqual(as_float('12.5'), 12.5)
        self.assertIsNone(as_float('bad'))
        self.assertEqual(normalize_caliber_mm(0.46), 460.0)
        self.assertEqual(normalize_caliber_mm(45.7), 457.0)
        self.assertEqual(normalize_caliber_mm(203), 203.0)
        self.assertIsNone(normalize_caliber_mm(0))

    def test_text_formatting_is_stable(self):
        self.assertEqual(normal_key(u'  PJSB018_Yamato_1944  '), 'pjsb018_yamato_1944')
        self.assertEqual(format_single_mm(460), u'460 mm')
        self.assertEqual(format_single_mm(54.9), u'54.9 mm')
        self.assertEqual(format_single_mm(None), u'? mm')
        self.assertEqual(format_mm([32, '25', 32, 57.5, 0]), u'25 mm/32 mm/57.5 mm')
        self.assertEqual(format_mm([]), u'? mm')


class OvermatchRuleTests(unittest.TestCase):
    def test_rule_limit_for_shell_types(self):
        self.assertAlmostEqual(rule_limit_for_ammo(AMMO_AP, 460, {}), 460 / 14.3)
        self.assertEqual(rule_limit_for_ammo(AMMO_HE, 152, {'mainGunHePenMm': 30}), 30)
        self.assertEqual(rule_limit_for_ammo(AMMO_HE, 152, {}), 25)
        self.assertEqual(rule_limit_for_ammo(AMMO_HE, None, {}), None)
        self.assertEqual(rule_limit_for_ammo(AMMO_SAP, 203, {'mainGunSapPenMm': 54.9}), 54.9)
        self.assertEqual(rule_limit_for_ammo(AMMO_SAP, 203, {}), None)

    def test_weapon_text_keeps_legacy_wording(self):
        self.assertIn('AP 460 mm', weapon_text(AMMO_AP, 460, 460 / 14.3))
        self.assertIn(u'\u78be\u538b', weapon_text(AMMO_AP, 460, 460 / 14.3))
        self.assertEqual(weapon_text(AMMO_AP, None, None), u'AP ? mm')
        self.assertEqual(weapon_text(AMMO_HE, None, 30), u'HE 30 mm \u7a7f\u6df1')
        self.assertEqual(weapon_text(AMMO_SAP, None, 54.9), u'SAP 54.9 mm \u7a7f\u6df1')

    def test_state_for_limit_matches_overmatch_cases(self):
        self.assertEqual(state_for_limit([32], 460 / 14.3), STATE_YES)
        self.assertEqual(state_for_limit([32], 457 / 14.3), STATE_NO)
        self.assertEqual(state_for_limit([25, 30], 406 / 14.3), STATE_PARTIAL)
        self.assertEqual(state_for_limit([], 100), STATE_UNKNOWN)
        self.assertEqual(state_for_limit([25], None), STATE_UNKNOWN)

    def test_flatten_values_keeps_unique_sorted_positive_numbers(self):
        group = {'values': [32, '25', 0, 32], 'bow': [16], 'stern': [19]}
        self.assertEqual(flatten_values(group), [16.0, 19.0, 25.0, 32.0])
        self.assertEqual(flatten_values({'main': [30], 'aft': [16]}), [16.0, 30.0])
        self.assertEqual(flatten_values(25), [25.0])

    def test_merge_states_and_state_text_selection(self):
        self.assertIs(state_text_for_ammo(AMMO_AP), STATE_TEXT_OVERMATCH)
        self.assertIs(state_text_for_ammo(AMMO_HE), STATE_TEXT_PEN)
        self.assertEqual(merge_states([STATE_YES, STATE_YES]), STATE_YES)
        self.assertEqual(merge_states([STATE_NO, STATE_NO]), STATE_NO)
        self.assertEqual(merge_states([STATE_YES, STATE_NO]), STATE_PARTIAL)
        self.assertEqual(merge_states([STATE_UNKNOWN]), STATE_UNKNOWN)

    def test_record_number_handles_missing_records(self):
        self.assertEqual(record_number({'mainGunCaliberMm': '406'}, 'mainGunCaliberMm'), 406.0)
        self.assertIsNone(record_number({}, 'mainGunCaliberMm'))
        self.assertIsNone(record_number(None, 'mainGunCaliberMm'))


class OvermatchPayloadTests(unittest.TestCase):
    def test_default_payload_returns_independent_copy(self):
        first = default_payload()
        second = default_payload()
        first['visible'] = True
        self.assertFalse(DEFAULT_PAYLOAD['visible'])
        self.assertFalse(second['visible'])

    def test_payload_builder_keeps_legacy_payload_shape(self):
        target_record = {
            'armor': {
                'bowStern': {'bow': [32], 'stern': [32]},
                'deck': {'values': [57]},
                'side': {'values': [32, 50]},
                'extendedBowSternBelt': {'present': False, 'values': [], 'bow': [], 'stern': []},
            }
        }

        payload = OvermatchPayloadBuilder().build_target_payload(
            'PJSB018_Yamato_1944',
            target_record,
            AMMO_AP,
            460,
            460 / 14.3,
        )

        self.assertTrue(payload['visible'])
        self.assertEqual(payload['targetName'], 'PJSB018_Yamato_1944')
        self.assertIn('AP 460 mm', payload['weaponText'])
        self.assertEqual(payload['caliberText'], payload['weaponText'])
        self.assertEqual(payload['bowSternColor'], STATE_COLOR[STATE_YES])
        self.assertEqual(payload['deckColor'], STATE_COLOR[STATE_NO])
        self.assertEqual(payload['sideColor'], STATE_COLOR[STATE_PARTIAL])
        self.assertEqual(payload['beltColor'], STATE_COLOR[STATE_YES])

    def test_payload_builder_handles_he_penetration_and_split_belt(self):
        target_record = {
            'armor': {
                'bowStern': {'values': [19]},
                'deck': {'values': [25]},
                'side': {'values': [30]},
                'extendedBowSternBelt': {
                    'present': True,
                    'bow': [25],
                    'stern': [40],
                },
            }
        }

        payload = OvermatchPayloadBuilder().build_target_payload(
            'PGSC110_Hindenburg',
            target_record,
            AMMO_HE,
            203,
            34,
        )

        self.assertIn('HE 34 mm', payload['weaponText'])
        self.assertEqual(payload['bowSternColor'], STATE_COLOR[STATE_YES])
        self.assertEqual(payload['deckColor'], STATE_COLOR[STATE_YES])
        self.assertEqual(payload['sideColor'], STATE_COLOR[STATE_YES])
        self.assertEqual(payload['beltColor'], STATE_COLOR[STATE_PARTIAL])

    def test_payload_builder_unknown_target_record_is_visible_but_unknown(self):
        payload = OvermatchPayloadBuilder().build_target_payload('Unknown target', None, AMMO_AP, 406, 406 / 14.3)
        self.assertTrue(payload['visible'])
        self.assertEqual(payload['targetName'], 'Unknown target')
        self.assertEqual(payload['bowSternColor'], STATE_COLOR[STATE_UNKNOWN])
        self.assertEqual(payload['deckColor'], STATE_COLOR[STATE_UNKNOWN])
        self.assertEqual(payload['sideColor'], STATE_COLOR[STATE_UNKNOWN])


class ArmorDatabaseTests(unittest.TestCase):
    def write_database(self, body):
        handle = tempfile.NamedTemporaryFile('w', suffix='.py', delete=False)
        try:
            handle.write(body)
            return handle.name
        finally:
            handle.close()

    def test_database_loads_and_finds_by_id_alias_and_name(self):
        path = self.write_database(textwrap.dedent("""
            DATABASE = {
                'meta': {'name': 'test'},
                'ships': {
                    '1001': {
                        'name': 'PJSB018_Yamato_1944',
                        'aliases': ['Yamato', 'PJSB018'],
                        'mainGunCaliberMm': 460,
                        'armor': {}
                    }
                }
            }
        """))
        try:
            db = ArmorDatabase(path)
            self.assertTrue(db.loaded)
            self.assertEqual(db.find({'id': 1001})['name'], 'PJSB018_Yamato_1944')
            self.assertEqual(db.find({'shipConfig': {'name': 'Yamato'}})['mainGunCaliberMm'], 460)
            self.assertEqual(db.find(Struct(publicInfo=Struct(name='pjsb018')))['name'], 'PJSB018_Yamato_1944')
            self.assertIsNone(db.find({'id': 9999}))
        finally:
            os.unlink(path)

    def test_database_reports_load_failure_without_throwing(self):
        db = ArmorDatabase(os.path.join(tempfile.gettempdir(), 'missing_armor_database.py'))
        self.assertFalse(db.loaded)
        self.assertEqual(db.ships, {})


class FakeArmorDb(object):
    def __init__(self, records):
        self.records = records

    def find(self, vehicle):
        return self.records.get(vehicle['name'])


class MainIntegrationTests(unittest.TestCase):
    def test_ammo_kind_detection_prefers_torpedo_sap_he_then_ap(self):
        assistant = Main.APOvermatchAssistant()
        assistant._selected_weapon_text = lambda: ''

        self.assertEqual(assistant._get_ammo_kind({'selectedAmmo': 'ammo_cs'}), AMMO_SAP)
        self.assertEqual(assistant._get_ammo_kind({'selectedAmmo': 'type_he'}), AMMO_HE)
        self.assertEqual(assistant._get_ammo_kind({'selectedAmmo': 'ammo_ap'}), AMMO_AP)
        self.assertEqual(assistant._get_ammo_kind({'selectedAmmo': 'torpedo'}), AMMO_TORPEDO)
        self.assertEqual(assistant._get_ammo_kind({'selectedAmmo': 'unknown'}), AMMO_AP)

    def test_main_caliber_uses_database_record_before_vehicle_scan(self):
        assistant = Main.APOvermatchAssistant()
        self.assertEqual(assistant._get_main_caliber({'shipConfig': {'artillery': {'caliber': 0.46}}}, {'mainGunCaliberMm': 406}), 406.0)
        self.assertEqual(assistant._get_main_caliber({'shipConfig': {'artillery': {'caliber': 0.46}}}, {}), 460.0)
        self.assertEqual(assistant._get_main_caliber({'mainGun': {'bulletDiameter': 0.203}}, {}), 203.0)

    def test_build_payload_integrates_vehicle_target_record_and_shell_rule(self):
        assistant = Main.APOvermatchAssistant()
        own = {'name': 'own', 'selectedAmmo': 'ammo_he'}
        target = {'name': 'target'}
        assistant._get_own_vehicle = lambda: own
        assistant._get_target_vehicle = lambda: target
        assistant._is_enemy_vehicle = lambda vehicle: vehicle is target
        assistant.armor_db = FakeArmorDb({
            'own': {'name': 'own', 'mainGunCaliberMm': 203, 'mainGunHePenMm': 34, 'armor': {}},
            'target': {
                'name': 'target-record',
                'armor': {
                    'bowStern': {'values': [25]},
                    'deck': {'values': [38]},
                    'side': {'values': [30]},
                    'extendedBowSternBelt': {'present': False},
                },
            },
        })

        payload = assistant._build_payload()
        self.assertTrue(payload['visible'])
        self.assertEqual(payload['targetName'], 'target-record')
        self.assertIn('HE 34 mm', payload['weaponText'])
        self.assertEqual(payload['deckColor'], STATE_COLOR[STATE_NO])

    def test_build_payload_hides_for_torpedoes_and_non_enemy_targets(self):
        assistant = Main.APOvermatchAssistant()
        own = {'name': 'own', 'selectedAmmo': 'torpedo'}
        assistant._get_own_vehicle = lambda: own
        assistant._get_target_vehicle = lambda: {'name': 'target'}
        assistant._is_enemy_vehicle = lambda vehicle: True
        assistant.armor_db = FakeArmorDb({})
        self.assertFalse(assistant._build_payload()['visible'])

        own['selectedAmmo'] = 'ammo_ap'
        assistant._is_enemy_vehicle = lambda vehicle: False
        self.assertFalse(assistant._build_payload()['visible'])

    def test_start_and_stop_manage_ui_entity_and_update_loop(self):
        previous_ui = Main.ui
        previous_vary = Main.Vary
        previous_bigworld = Main.BigWorld
        try:
            fake_ui = FakeUi()
            fake_vary = FakeVary()
            Main.ui = fake_ui
            Main.Vary = fake_vary
            Main.BigWorld = Struct(callback=lambda interval, callback: None)

            assistant = RuntimeAssistant()
            assistant.start()

            self.assertTrue(assistant.active)
            self.assertEqual(assistant.ui_entity_id, 42)
            self.assertEqual(fake_ui.added[0][1], COMPONENT_KEY)
            self.assertIs(assistant.update_task, fake_vary.task)

            assistant.stop()
            self.assertFalse(assistant.active)
            self.assertEqual(fake_vary.stopped, [fake_vary.task])
            self.assertEqual(fake_ui.deleted, [42])
        finally:
            Main.ui = previous_ui
            Main.Vary = previous_vary
            Main.BigWorld = previous_bigworld


class RuntimeAssistant(Main.APOvermatchAssistant):
    def _register_events(self):
        self.events_registered = True

    def _load_runtime(self):
        self.runtime_loaded = True
        return True

    def _build_payload(self):
        return default_payload()


class FakeUi(object):
    def __init__(self):
        self.added = []
        self.updated = []
        self.deleted = []

    def createUiElement(self):
        return 42

    def addDataComponentWithId(self, entity_id, component_key, payload):
        self.added.append((entity_id, component_key, payload))

    def updateUiElementData(self, entity_id, payload):
        self.updated.append((entity_id, payload))

    def deleteUiElement(self, entity_id):
        self.deleted.append(entity_id)


class FakeVary(object):
    def __init__(self):
        self.task = object()
        self.started = []
        self.stopped = []

    def start(self, interval, callback):
        self.started.append((interval, callback))
        return self.task

    def stop(self, task):
        self.stopped.append(task)


if __name__ == '__main__':
    unittest.main()
