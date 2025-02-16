import os, loguru, configparser

class Common:
    def __init__(self):
        self._config_path = f"{os.path.dirname(__file__)}/config.ini"
        print(self._config_path)
        self._config = configparser.ConfigParser()
        self._config.read(self._config_path)
        print([i for i in self._config.sections()])

c = Common()
