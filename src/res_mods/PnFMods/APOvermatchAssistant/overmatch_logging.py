# -*- coding: utf-8 -*-

from overmatch_constants import MOD_NAME


def _wows_utils():
    try:
        import utils
        return utils
    except Exception:
        return None


def log(level, message):
    try:
        text = '[{}] {}: {}'.format(MOD_NAME, level, message)
        game_utils = _wows_utils()
        if game_utils:
            try:
                if level == 'ERROR':
                    game_utils.logError(text)
                else:
                    game_utils.logInfo(text)
                return
            except Exception:
                pass
        try:
            print(text)
        except Exception:
            pass
    except Exception:
        pass


def log_info(message):
    log('INFO', message)


def log_error(message):
    log('ERROR', message)
