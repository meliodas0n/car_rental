import os, pathlib, configparser

class Common:
  def __init__(self) -> None:
    self._config_path: str = f"{os.path.dirname(__file__)}/config.ini"
    self._config: configparser.ConfigParser = configparser.ConfigParser()
    self._config.read(self._config_path)
    print([i for i in self._config.sections()])

Common()
