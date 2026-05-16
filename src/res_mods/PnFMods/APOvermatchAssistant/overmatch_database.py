# -*- coding: utf-8 -*-

from overmatch_logging import log_error, log_info
from overmatch_utils import get_path, normal_key


class ArmorDatabase(object):
    def __init__(self, database_path=None):
        self.database_path = database_path
        self.meta = {}
        self.ships = {}
        self.aliases = {}
        self.loaded = False
        self.load()

    def load(self):
        path = self.database_path or self._default_database_path()
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
            self.aliases = self._build_aliases(self.ships)
            self.loaded = True
            log_info('loaded armor database: {} ships'.format(len(self.ships)))
        except Exception as exc:
            self.loaded = False
            log_error('failed to load armor database: {}'.format(exc))

    def find(self, vehicle):
        keys = self._vehicle_keys(vehicle)
        for key in keys:
            ship_id = str(key)
            if ship_id in self.ships:
                return self.ships[ship_id]
            alias = normal_key(key)
            if alias in self.aliases:
                return self.ships.get(self.aliases[alias])
        return None

    def _default_database_path(self):
        try:
            path = __file__
            idx = max(path.rfind('/'), path.rfind('\\'))
            base = path[:idx] if idx >= 0 else '.'
        except Exception:
            base = '.'
        return base + '/data/armor_overmatch.py'

    def _build_aliases(self, ships):
        aliases = {}
        for key, ship in ships.items():
            aliases[str(key)] = key
            for alias in ship.get('aliases', []):
                aliases[normal_key(alias)] = key
            if ship.get('name'):
                aliases[normal_key(ship.get('name'))] = key
        return aliases

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
            value = get_path(vehicle, path)
            if value is not None and value not in keys:
                keys.append(value)
        return keys
