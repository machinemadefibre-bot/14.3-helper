# -*- coding: utf-8 -*-
API_VERSION = 'API_v1.0'
MOD_NAME = 'APOvermatchAssistant'
MOD_VERSION = '0.2.26'

try:
    unicode
except NameError:
    unicode = str

BigWorld = None
BWPersonality = None
ui = None
Vary = None


COMPONENT_KEY = 'modOvermatchAssistant'
UPDATE_INTERVAL = 0.2
OVERMATCH_DIVISOR = 14.3
INF = 1000000
OBSERVER_TEAM_ID = 0

AMMO_AP = 'AP'
AMMO_HE = 'HE'
AMMO_SAP = 'SAP'
AMMO_TORPEDO = 'TORPEDO'

STATE_YES = 'yes'
STATE_PARTIAL = 'partial'
STATE_NO = 'no'
STATE_UNKNOWN = 'unknown'

TXT_YES_OVERMATCH = u'\u53ef\u78be\u538b'
TXT_PARTIAL_OVERMATCH = u'\u90e8\u5206\u53ef\u78be\u538b'
TXT_NO_OVERMATCH = u'\u4e0d\u53ef\u78be\u538b'
TXT_YES_PEN = u'\u53ef\u51fb\u7a7f'
TXT_PARTIAL_PEN = u'\u90e8\u5206\u53ef\u51fb\u7a7f'
TXT_NO_PEN = u'\u4e0d\u53ef\u51fb\u7a7f'
TXT_UNKNOWN = u'\u672a\u77e5'
TXT_BOW_STERN = u'\u5934\u5c3e'
TXT_BOW = u'\u824f'
TXT_STERN = u'\u8249'
TXT_DECK = u'\u7532\u677f'
TXT_SIDE = u'\u4fa7\u677f'
TXT_BELT = u'\u884d\u751f\u5e26/\u7834\u51b0\u5e26'
TXT_NO_BELT = u'\u65e0'
TXT_HAS_BELT = u'\u6709'
TXT_TARGET = u'\u76ee\u6807'
TXT_OVERMATCH_LIMIT = u'\u78be\u538b'
TXT_PENETRATION = u'\u7a7f\u6df1'

STATE_TEXT_OVERMATCH = {
    STATE_YES: TXT_YES_OVERMATCH,
    STATE_PARTIAL: TXT_PARTIAL_OVERMATCH,
    STATE_NO: TXT_NO_OVERMATCH,
    STATE_UNKNOWN: TXT_UNKNOWN,
}

STATE_TEXT_PEN = {
    STATE_YES: TXT_YES_PEN,
    STATE_PARTIAL: TXT_PARTIAL_PEN,
    STATE_NO: TXT_NO_PEN,
    STATE_UNKNOWN: TXT_UNKNOWN,
}

STATE_COLOR = {
    STATE_YES: 0x76D672,
    STATE_PARTIAL: 0xFFCC66,
    STATE_NO: 0xFF6666,
    STATE_UNKNOWN: 0xB8B8B8,
}

DEFAULT_PAYLOAD = {
    'visible': False,
    'targetName': '',
    'weaponText': '',
    'caliberText': '',
    'bowSternText': TXT_BOW_STERN + u': ' + TXT_UNKNOWN,
    'bowSternColor': STATE_COLOR[STATE_UNKNOWN],
    'deckText': TXT_DECK + u': ' + TXT_UNKNOWN,
    'deckColor': STATE_COLOR[STATE_UNKNOWN],
    'sideText': TXT_SIDE + u': ' + TXT_UNKNOWN,
    'sideColor': STATE_COLOR[STATE_UNKNOWN],
    'beltText': TXT_BELT + u': ' + TXT_UNKNOWN,
    'beltColor': STATE_COLOR[STATE_UNKNOWN],
}


def _log(level, message):
    try:
        text = '[{}] {}: {}'.format(MOD_NAME, level, message)
        try:
            if level == 'ERROR':
                utils.logError(text)
            else:
                utils.logInfo(text)
            return
        except Exception:
            pass
        try:
            print(text)
        except Exception:
            pass
    except Exception:
        pass


def _log_info(message):
    _log('INFO', message)


def _log_error(message):
    _log('ERROR', message)


def _safe_getattr(obj, name, default=None):
    try:
        if obj is None:
            return default
        if isinstance(obj, dict):
            return obj.get(name, default)
        return getattr(obj, name, default)
    except Exception:
        return default


def _as_float(value, default=None):
    try:
        if value is None:
            return default
        return float(value)
    except Exception:
        return default


def _normalize_caliber_mm(value):
    caliber = _as_float(value)
    if caliber is None or caliber <= 0:
        return None
    if caliber < 5:
        caliber *= 1000.0
    elif caliber < 80:
        caliber *= 10.0
    return round(caliber, 1)


def _format_mm(values):
    clean = []
    for value in values:
        mm = _as_float(value)
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


def _format_single_mm(value):
    mm = _as_float(value)
    if mm is None or mm <= 0:
        return u'? mm'
    if abs(mm - int(mm)) < 0.01:
        return u'{} mm'.format(int(mm))
    return u'{:.1f} mm'.format(mm)


def _flatten_values(group):
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
        mm = _as_float(item)
        if mm is not None and mm > 0 and mm not in values:
            values.append(mm)
    values.sort()
    return values


def _state_for_limit(values, limit_mm):
    if not values or limit_mm is None:
        return STATE_UNKNOWN
    hits = [limit_mm >= value for value in values]
    if all(hits):
        return STATE_YES
    if any(hits):
        return STATE_PARTIAL
    return STATE_NO


class ArmorDatabase(object):
    def __init__(self):
        self.meta = {}
        self.ships = {}
        self.aliases = {}
        self.loaded = False
        self.load()

    def load(self):
        path = self._database_path()
        try:
            namespace = {}
            try:
                execfile(path, namespace)
            except NameError:
                with open(path, 'rb') as handle:
                    code = handle.read()
                exec(compile(code, path, 'exec'), namespace)
            data = namespace.get('DATABASE', {})
            self.meta = data.get('meta', {})
            self.ships = data.get('ships', {})
            self.aliases = {}
            for key, ship in self.ships.items():
                self.aliases[str(key)] = key
                for alias in ship.get('aliases', []):
                    self.aliases[self._normal_key(alias)] = key
                if ship.get('name'):
                    self.aliases[self._normal_key(ship.get('name'))] = key
            self.loaded = True
            _log_info('loaded armor database: {} ships'.format(len(self.ships)))
        except Exception as exc:
            self.loaded = False
            _log_error('failed to load armor database: {}'.format(exc))

    def _database_path(self):
        try:
            path = __file__
            idx = max(path.rfind('/'), path.rfind('\\'))
            base = path[:idx] if idx >= 0 else '.'
        except Exception:
            base = '.'
        return base + '/data/armor_overmatch.py'

    def _normal_key(self, value):
        try:
            return unicode(value).strip().lower()
        except Exception:
            try:
                return str(value).strip().lower()
            except Exception:
                return ''

    def find(self, vehicle):
        keys = self._vehicle_keys(vehicle)
        for key in keys:
            skey = str(key)
            if skey in self.ships:
                return self.ships[skey]
            nkey = self._normal_key(key)
            if nkey in self.aliases:
                return self.ships.get(self.aliases[nkey])
        return None

    def _vehicle_keys(self, vehicle):
        keys = []
        paths = (
            ('shipConfig', 'shipId'),
            ('shipConfig', 'id'),
            ('shipConfig', 'name'),
            ('shipConfig', 'index'),
            ('shipConfig', 'typeinfo', 'name'),
            ('typeDescriptor', 'type', 'name'),
            ('typeDescriptor', 'type', 'id'),
            ('publicInfo', 'name'),
            ('name',),
            ('id',),
        )
        for path in paths:
            value = self._get_path(vehicle, path)
            if value is not None and value not in keys:
                keys.append(value)
        return keys

    def _get_path(self, obj, path):
        cur = obj
        for part in path:
            cur = _safe_getattr(cur, part)
            if cur is None:
                return None
        return cur


class APOvermatchAssistant(object):
    def __init__(self):
        self.db = None
        self.entity_id = None
        self.camera = None
        self.vary = None
        self.active = False
        self.last_payload = None
        self.runtime_loaded = False

        _log_info('registered for API_v2 lifecycle')

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
        _log_info('runtime imports ui={} bigworld={} bwpersonality={} vary={}'.format(
            bool(ui), bool(BigWorld), bool(BWPersonality), bool(Vary)
        ))
        if not self.runtime_loaded:
            _log_error('runtime not ready: ui and BigWorld are required')
        return self.runtime_loaded

    def start(self, *args):
        try:
            if not self._load_runtime():
                return
            if self.entity_id is not None:
                self.stop()
            self.active = True
            self.entity_id = ui.createUiElement()
            payload = dict(DEFAULT_PAYLOAD)
            ui.addDataComponentWithId(self.entity_id, COMPONENT_KEY, payload)
            self.last_payload = payload
            self.camera = self._get_camera()
            self.update(0)
            self._start_loop()
            _log_info('started entity_id={}'.format(self.entity_id))
        except Exception as exc:
            _log_error('start failed: {}'.format(exc))

    def on_battle_start(self, *args):
        self.start(*args)

    def stop(self, *args):
        self.active = False
        try:
            if Vary and self.vary:
                Vary.stop(self.vary)
            self.vary = None
        except Exception:
            pass
        try:
            if self.entity_id is not None:
                ui.deleteUiElement(self.entity_id)
        except Exception:
            pass
        self.entity_id = None
        self.camera = None
        self.last_payload = None
        _log_info('stopped')

    def on_battle_quit(self, *args):
        self.stop(*args)

    def kill(self, *args):
        self.stop(*args)

    def _start_loop(self):
        if Vary:
            self.vary = Vary.start(UPDATE_INTERVAL, self.update)
            _log_info('update loop started with Vary')
            return
        if BigWorld:
            BigWorld.callback(UPDATE_INTERVAL, self._callback_update)
            _log_info('update loop started with BigWorld.callback')

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
            if payload != self.last_payload and self.entity_id is not None:
                ui.updateUiElementData(self.entity_id, payload)
                self.last_payload = payload
        except Exception as exc:
            _log_error('update failed: {}'.format(exc))

    def _build_payload(self):
        if self.db is None:
            self.db = ArmorDatabase()

        own = self._get_own_vehicle()
        ammo_kind = self._get_ammo_kind(own)
        if ammo_kind == AMMO_TORPEDO:
            return dict(DEFAULT_PAYLOAD)

        target = self._get_target_vehicle()
        if not self._is_enemy_vehicle(target):
            return dict(DEFAULT_PAYLOAD)

        own_record = self.db.find(own) if own is not None else None
        caliber = self._get_main_caliber(own, own_record)
        limit = self._get_rule_limit(ammo_kind, caliber, own_record)
        target_record = self.db.find(target)

        payload = dict(DEFAULT_PAYLOAD)
        payload['visible'] = True
        payload['targetName'] = self._display_ship_name(target, target_record)
        payload['weaponText'] = self._weapon_text(ammo_kind, caliber, limit)
        payload['caliberText'] = payload['weaponText']

        armor = target_record.get('armor', {}) if target_record else {}
        state_text = STATE_TEXT_OVERMATCH if ammo_kind == AMMO_AP else STATE_TEXT_PEN
        self._apply_bow_stern(payload, armor.get('bowStern'), limit, state_text)
        self._apply_simple(payload, 'deck', TXT_DECK, armor.get('deck'), limit, state_text)
        self._apply_simple(payload, 'side', TXT_SIDE, armor.get('side'), limit, state_text)
        self._apply_belt(payload, armor.get('extendedBowSternBelt'), limit, state_text)
        return payload

    def _get_rule_limit(self, ammo_kind, caliber, own_record):
        if ammo_kind == AMMO_AP:
            if caliber is None:
                return None
            return caliber / OVERMATCH_DIVISOR
        if ammo_kind == AMMO_HE:
            value = self._record_number(own_record, 'mainGunHePenMm')
            if value is not None:
                return value
            if caliber is not None:
                return int(caliber / 6.0)
            return None
        if ammo_kind == AMMO_SAP:
            return self._record_number(own_record, 'mainGunSapPenMm')
        return None

    def _weapon_text(self, ammo_kind, caliber, limit):
        if ammo_kind == AMMO_AP:
            if caliber is None:
                return u'AP ? mm'
            return u'AP {} ({} {})'.format(_format_single_mm(caliber), TXT_OVERMATCH_LIMIT, _format_single_mm(limit))
        if ammo_kind == AMMO_HE:
            return u'HE {} {}'.format(_format_single_mm(limit), TXT_PENETRATION)
        if ammo_kind == AMMO_SAP:
            return u'SAP {} {}'.format(_format_single_mm(limit), TXT_PENETRATION)
        return u'?'

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
            if not vehicle or _safe_getattr(vehicle, 'className') != 'Vehicle':
                return False
            player = BigWorld.player() if BigWorld else None
            own_team = _safe_getattr(player, 'teamId')
            if own_team != OBSERVER_TEAM_ID and own_team == _safe_getattr(vehicle, 'teamId'):
                return False
            return True
        except Exception:
            return False

    def _get_main_caliber(self, vehicle, record=None):
        caliber = self._record_number(record, 'mainGunCaliberMm')
        if caliber:
            return _normalize_caliber_mm(caliber)

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
            value = self._get_path(vehicle, path)
            caliber = _normalize_caliber_mm(value)
            if caliber:
                return caliber
        return self._scan_for_caliber(vehicle)

    def _record_number(self, record, name):
        if not record:
            return None
        return _as_float(record.get(name))

    def _scan_for_caliber(self, obj, depth=0):
        if depth > 3 or obj is None:
            return None
        if isinstance(obj, dict):
            items = obj.items()
        elif isinstance(obj, (list, tuple)):
            items = enumerate(obj)
        else:
            for name in ('caliber', 'gunCaliber', 'mainGunCaliber', 'bulletDiameter', 'bulletDiametr'):
                value = _safe_getattr(obj, name)
                caliber = _normalize_caliber_mm(value)
                if caliber:
                    return caliber
            return None
        for key, value in items:
            key_text = str(key).lower()
            if 'caliber' in key_text or 'diametr' in key_text or 'diameter' in key_text:
                caliber = _normalize_caliber_mm(value)
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
            value = self._get_path(vehicle, path)
            if value is not None:
                return str(value)
        try:
            player = BigWorld.player() if BigWorld else None
            for attr in ('selectedAmmo', 'selectedAmmoType', 'ammoType', 'currentAmmo', 'currentShell'):
                value = _safe_getattr(player, attr)
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
                value = self._get_path(player, path)
                if value is not None:
                    return str(value)
        except Exception:
            pass
        return ''

    def _get_path(self, obj, path):
        cur = obj
        for part in path:
            cur = _safe_getattr(cur, part)
            if cur is None:
                return None
        return cur

    def _apply_bow_stern(self, payload, group, limit, state_text):
        if isinstance(group, dict) and ('bow' in group or 'stern' in group):
            bow = _flatten_values(group.get('bow') or group.get('fore') or group.get('values'))
            stern = _flatten_values(group.get('stern') or group.get('aft') or group.get('values'))
            bow_state = _state_for_limit(bow, limit)
            stern_state = _state_for_limit(stern, limit)
            state = self._merge_states([bow_state, stern_state])
            payload['bowSternText'] = u'{}: {} {} / {} {} ({} / {})'.format(
                TXT_BOW_STERN,
                TXT_BOW,
                state_text[bow_state],
                TXT_STERN,
                state_text[stern_state],
                _format_mm(bow),
                _format_mm(stern),
            )
            payload['bowSternColor'] = STATE_COLOR[state]
            return
        values = _flatten_values(group)
        state = _state_for_limit(values, limit)
        payload['bowSternText'] = u'{}: {} ({})'.format(TXT_BOW_STERN, state_text[state], _format_mm(values))
        payload['bowSternColor'] = STATE_COLOR[state]

    def _apply_simple(self, payload, key, label, group, limit, state_text):
        values = _flatten_values(group)
        state = _state_for_limit(values, limit)
        payload[key + 'Text'] = u'{}: {} ({})'.format(label, state_text[state], _format_mm(values))
        payload[key + 'Color'] = STATE_COLOR[state]

    def _apply_belt(self, payload, group, limit, state_text):
        present = True
        if not group:
            present = False
        elif isinstance(group, dict) and 'present' in group:
            present = bool(group.get('present'))

        if not present:
            payload['beltText'] = u'{}: {}'.format(TXT_BELT, TXT_NO_BELT)
            payload['beltColor'] = STATE_COLOR[STATE_YES]
            return

        values = _flatten_values(group)
        state = _state_for_limit(values, limit)
        payload['beltText'] = u'{}: {} - {} ({})'.format(TXT_BELT, TXT_HAS_BELT, state_text[state], _format_mm(values))
        payload['beltColor'] = STATE_COLOR[state]

    def _merge_states(self, states):
        filtered = [state for state in states if state != STATE_UNKNOWN]
        if not filtered:
            return STATE_UNKNOWN
        if all(state == STATE_YES for state in filtered):
            return STATE_YES
        if all(state == STATE_NO for state in filtered):
            return STATE_NO
        return STATE_PARTIAL

    def _target_name(self, vehicle):
        for path in (('publicInfo', 'name'), ('shipConfig', 'name'), ('name',)):
            value = self._get_path(vehicle, path)
            if value:
                return value
        return TXT_TARGET

    def _display_ship_name(self, vehicle, record):
        if record and record.get('name'):
            return record.get('name')
        return self._target_name(vehicle)


gAPOvermatchAssistant = APOvermatchAssistant()


def init(*args):
    _log_info('module init')
    gAPOvermatchAssistant.start(*args)


def start(*args):
    gAPOvermatchAssistant.start(*args)


def stop(*args):
    gAPOvermatchAssistant.stop(*args)


def fini(*args):
    gAPOvermatchAssistant.stop(*args)


def kill(*args):
    gAPOvermatchAssistant.kill(*args)
