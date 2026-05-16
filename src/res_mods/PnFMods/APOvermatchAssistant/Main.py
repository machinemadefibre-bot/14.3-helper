# -*- coding: utf-8 -*-

import sys

try:
    _MODULE_DIR_INDEX = max(__file__.rfind('/'), __file__.rfind('\\'))
    _MODULE_DIR = __file__[:_MODULE_DIR_INDEX] if _MODULE_DIR_INDEX >= 0 else ''
    if _MODULE_DIR and _MODULE_DIR not in sys.path:
        sys.path.insert(0, _MODULE_DIR)
except Exception:
    pass

from overmatch_constants import (
    AMMO_AP,
    AMMO_HE,
    AMMO_SAP,
    AMMO_TORPEDO,
    API_VERSION,
    COMPONENT_KEY,
    INF,
    MOD_NAME,
    MOD_VERSION,
    OBSERVER_TEAM_ID,
    TXT_TARGET,
    UPDATE_INTERVAL,
)
from overmatch_database import ArmorDatabase
from overmatch_logging import log_error, log_info
from overmatch_payload import OvermatchPayloadBuilder, default_payload
from overmatch_rules import record_number, rule_limit_for_ammo
from overmatch_utils import get_path, normalize_caliber_mm, safe_getattr

BigWorld = None
BWPersonality = None
events = None
ui = None
Vary = None


class APOvermatchAssistant(object):
    def __init__(self):
        self.armor_db = None
        self.payload_builder = OvermatchPayloadBuilder()
        self.ui_entity_id = None
        self.camera = None
        self.update_task = None
        self.active = False
        self.last_payload = None
        self.runtime_loaded = False
        self.events_registered = False

        self._register_events()

    def _register_events(self):
        global events
        if self.events_registered:
            return
        try:
            import events as _events
            events = _events
            events.onBattleStart(self.on_battle_start)
            events.onBattleQuit(self.on_battle_quit)
            self.events_registered = True
            log_info('registered battle lifecycle events')
        except Exception as exc:
            log_error('failed to register battle lifecycle events: {}'.format(exc))

    def _load_runtime(self):
        global BigWorld, BWPersonality, ui, Vary
        if self.runtime_loaded:
            return True
        try:
            import BigWorld as _BigWorld
            BigWorld = _BigWorld
        except Exception:
            BigWorld = None
        try:
            import BWPersonality as _BWPersonality
            BWPersonality = _BWPersonality
        except Exception:
            BWPersonality = None
        try:
            import ui as _ui
            ui = _ui
        except Exception:
            ui = None
        try:
            from ModsShell.API_v_1_0.battleGate import Vary as _Vary
            Vary = _Vary
        except Exception:
            Vary = None

        self.runtime_loaded = bool(BigWorld and ui)
        log_info('runtime imports ui={} bigworld={} bwpersonality={} vary={}'.format(
            bool(ui), bool(BigWorld), bool(BWPersonality), bool(Vary)
        ))
        if not self.runtime_loaded:
            log_error('runtime not ready: ui and BigWorld are required')
        return self.runtime_loaded

    def start(self, *args):
        try:
            if not self._load_runtime():
                return
            if self.ui_entity_id is not None:
                self.stop()
            self.active = True
            self.ui_entity_id = ui.createUiElement()
            payload = default_payload()
            ui.addDataComponentWithId(self.ui_entity_id, COMPONENT_KEY, payload)
            self.last_payload = payload
            self.camera = self._get_camera()
            self.update(0)
            self._start_loop()
            log_info('started entity_id={}'.format(self.ui_entity_id))
        except Exception as exc:
            log_error('start failed: {}'.format(exc))

    def on_battle_start(self, *args):
        self.start(*args)

    def onBattleStart(self, *args):
        self.on_battle_start(*args)

    def stop(self, *args):
        self.active = False
        try:
            if Vary and self.update_task:
                Vary.stop(self.update_task)
            self.update_task = None
        except Exception:
            pass
        try:
            if ui and self.ui_entity_id is not None:
                ui.deleteUiElement(self.ui_entity_id)
        except Exception:
            pass
        self.ui_entity_id = None
        self.camera = None
        self.last_payload = None
        log_info('stopped')

    def on_battle_quit(self, *args):
        self.stop(*args)

    def onBattleQuit(self, *args):
        self.on_battle_quit(*args)

    def kill(self, *args):
        self.stop(*args)

    def _start_loop(self):
        if Vary:
            self.update_task = Vary.start(UPDATE_INTERVAL, self.update)
            log_info('update loop started with Vary')
            return
        if BigWorld:
            BigWorld.callback(UPDATE_INTERVAL, self._callback_update)
            log_info('update loop started with BigWorld.callback')

    def _callback_update(self):
        if not self.active:
            return
        self.update(UPDATE_INTERVAL)
        try:
            if BigWorld:
                BigWorld.callback(UPDATE_INTERVAL, self._callback_update)
        except Exception:
            pass

    def update(self, dt=0):
        try:
            payload = self._build_payload()
            if payload != self.last_payload and self.ui_entity_id is not None:
                ui.updateUiElementData(self.ui_entity_id, payload)
                self.last_payload = payload
        except Exception as exc:
            log_error('update failed: {}'.format(exc))

    def _build_payload(self):
        if self.armor_db is None:
            self.armor_db = ArmorDatabase()

        own_vehicle = self._get_own_vehicle()
        ammo_kind = self._get_ammo_kind(own_vehicle)
        if ammo_kind == AMMO_TORPEDO:
            return default_payload()

        target_vehicle = self._get_target_vehicle()
        if not self._is_enemy_vehicle(target_vehicle):
            return default_payload()

        own_record = self.armor_db.find(own_vehicle) if own_vehicle is not None else None
        main_caliber = self._get_main_caliber(own_vehicle, own_record)
        rule_limit = rule_limit_for_ammo(ammo_kind, main_caliber, own_record)
        target_record = self.armor_db.find(target_vehicle)
        target_name = self._display_ship_name(target_vehicle, target_record)

        return self.payload_builder.build_target_payload(
            target_name,
            target_record,
            ammo_kind,
            main_caliber,
            rule_limit,
        )

    def _get_camera(self):
        try:
            if BWPersonality:
                return BWPersonality.Camera.get()
        except Exception:
            return None
        return None

    def _get_target_vehicle(self):
        if not self.camera:
            self.camera = self._get_camera()
        try:
            if self.camera:
                return self.camera.getAimAssistEntity(INF, 0, True)
        except Exception:
            return None
        return None

    def _get_own_vehicle(self):
        try:
            player = BigWorld.player() if BigWorld else None
            if player and hasattr(player, 'getOwnVehicle'):
                return player.getOwnVehicle()
        except Exception:
            pass
        return None

    def _is_enemy_vehicle(self, vehicle):
        try:
            if not vehicle or safe_getattr(vehicle, 'className') != 'Vehicle':
                return False
            player = BigWorld.player() if BigWorld else None
            own_team = safe_getattr(player, 'teamId')
            if own_team != OBSERVER_TEAM_ID and own_team == safe_getattr(vehicle, 'teamId'):
                return False
            return True
        except Exception:
            return False

    def _get_main_caliber(self, vehicle, record=None):
        caliber = record_number(record, 'mainGunCaliberMm')
        if caliber:
            return normalize_caliber_mm(caliber)

        paths = (
            ('shipConfig', 'artillery', 'caliber'),
            ('shipConfig', 'artillery', 'gunCaliber'),
            ('shipConfig', 'artillery', 'mainGunCaliber'),
            ('shipConfig', 'artillery', 'mainGun', 'caliber'),
            ('shipConfig', 'artillery', 'mainGun', 'gunCaliber'),
            ('shipConfig', 'mainGun', 'caliber'),
            ('typeDescriptor', 'artillery', 'caliber'),
        )
        for path in paths:
            value = get_path(vehicle, path)
            caliber = normalize_caliber_mm(value)
            if caliber:
                return caliber
        return self._scan_for_caliber(vehicle)

    def _scan_for_caliber(self, obj, depth=0):
        if depth > 3 or obj is None:
            return None
        if isinstance(obj, dict):
            items = list(obj.items())
        elif isinstance(obj, (list, tuple)):
            items = list(enumerate(obj))
        else:
            for name in ('caliber', 'gunCaliber', 'mainGunCaliber', 'bulletDiameter', 'bulletDiametr'):
                value = safe_getattr(obj, name)
                caliber = normalize_caliber_mm(value)
                if caliber:
                    return caliber
            return None
        for key, value in items:
            key_text = str(key).lower()
            if 'caliber' in key_text or 'diametr' in key_text or 'diameter' in key_text:
                caliber = normalize_caliber_mm(value)
                if caliber:
                    return caliber
        for key, value in items:
            key_text = str(key).lower()
            if any(token in key_text for token in ('artillery', 'maingun', 'gun', 'ammo', 'shell')):
                caliber = self._scan_for_caliber(value, depth + 1)
                if caliber:
                    return caliber
        return None

    def _get_ammo_kind(self, vehicle):
        text = (self._selected_ammo_text(vehicle) + ' ' + self._selected_weapon_text()).lower()
        words = text.replace('_', ' ').replace('-', ' ').replace('.', ' ').split()
        if any(token in text for token in ('torpedo', 'torp', 'depthcharge', 'depth_charge', 'sea_mine')):
            return AMMO_TORPEDO
        if 'sap' in words or 'cs' in words or any(token in text for token in ('ammo_cs', 'type_cs')):
            return AMMO_SAP
        if 'he' in words:
            return AMMO_HE
        if 'ammo_he' in text or 'type_he' in text:
            return AMMO_HE
        if 'ap' in words or 'ammo_ap' in text or 'type_ap' in text:
            return AMMO_AP
        return AMMO_AP

    def _selected_ammo_text(self, vehicle):
        paths = (
            ('selectedAmmo',),
            ('selectedAmmoType',),
            ('ammoType',),
            ('currentAmmo',),
            ('currentShell',),
            ('weaponController', 'selectedAmmo'),
            ('weaponController', 'ammoType'),
            ('shipConfig', 'selectedAmmo'),
        )
        for path in paths:
            value = get_path(vehicle, path)
            if value is not None:
                return str(value)
        try:
            player = BigWorld.player() if BigWorld else None
            for attr in ('selectedAmmo', 'selectedAmmoType', 'ammoType', 'currentAmmo', 'currentShell'):
                value = safe_getattr(player, attr)
                if value is not None:
                    return str(value)
        except Exception:
            pass
        return ''

    def _selected_weapon_text(self):
        try:
            player = BigWorld.player() if BigWorld else None
            candidates = (
                ('inputHandler', 'ctrl', 'name'),
                ('inputHandler', 'ctrl', 'modeName'),
                ('inputHandler', 'ctrl', 'weaponName'),
                ('inputHandler', 'ctrl', 'selectedWeapon'),
                ('inputHandler', 'ctrl', 'currentWeapon'),
                ('inputHandler', 'ctrl', 'cameraType'),
                ('weaponController', 'selectedWeapon'),
                ('weaponController', 'weaponName'),
            )
            for path in candidates:
                value = get_path(player, path)
                if value is not None:
                    return str(value)
        except Exception:
            pass
        return ''

    def _target_name(self, vehicle):
        for path in (('publicInfo', 'name'), ('shipConfig', 'name'), ('name',)):
            value = get_path(vehicle, path)
            if value:
                return value
        return TXT_TARGET

    def _display_ship_name(self, vehicle, record):
        if record and record.get('name'):
            return record.get('name')
        return self._target_name(vehicle)


gAPOvermatchAssistant = APOvermatchAssistant()


def init(*args):
    log_info('module init')
    gAPOvermatchAssistant.start(*args)


def start(*args):
    gAPOvermatchAssistant.start(*args)


def stop(*args):
    gAPOvermatchAssistant.stop(*args)


def fini(*args):
    gAPOvermatchAssistant.stop(*args)


def kill(*args):
    gAPOvermatchAssistant.kill(*args)
