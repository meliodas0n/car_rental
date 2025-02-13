import os, loguru, configparser

class Common:
    def __init__(self):
        self.__config_path = f"{os.path.dirname(__file__)}/config.ini"
        self.__config = configparser.ConfigParser()
        self.__config.read(self.__config_path)
