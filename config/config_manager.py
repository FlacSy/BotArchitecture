import configparser
import os

class ConfigManager:
    def __init__(self, mode: str = 'development'):

        """
        Параметр `mode` это режим для конфигурации. Возможные значения: 'development' для розроботки, 'production' для продакшина
        """
        
        self.mode = mode
        self.config = configparser.ConfigParser()
        self.load_config()

    def load_config(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_path, self.mode)
        config_path = os.path.join(config_path, 'config.ini')

        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found at: {config_path}")

        self.config.read(config_path, encoding='utf-8')

    def get_config_value(self, section, option):
        return self.config.get(section, option)
