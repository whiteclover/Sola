

class Config(object):


    def __init__(self):
        self._config = dict()

    def get(self, key, default=None):
        return self._config.get(key, default)

    def set(self, key, value):
        return self._config.set(key, value)

    def update(self, config):
        self._config.update(config)


config = Config()