import json
import os

class ConfigManager:
    def __init__(self):
        self.config = {}
        self.load_config()

    def load_config(self):
        config_path = "./local/config.json"

        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found at: {config_path}")

        with open(config_path, 'r', encoding='utf-8') as file:
            self.config = json.load(file)

    def get_config_value(self, section, option):
        if section in self.config and option in self.config[section]:
            return self.config[section][option]
        else:
            raise KeyError(f"Section '{section}' or option '{option}' not found in config.")
