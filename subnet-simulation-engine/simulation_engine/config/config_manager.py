import json

class ConfigManager:
    @staticmethod
    def load_config(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
