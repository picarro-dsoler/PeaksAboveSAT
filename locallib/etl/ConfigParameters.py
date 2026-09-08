import json
class ConfigParameters:
    def __init__(self, config_file):
        self.config_file = config_file
        self.readConfigFile()

    def readConfigFile(self):
        with open(self.config_file, 'r') as file:
            config = json.load(file)
        
        # Set a dict called vals with the json pairs
        self.vals = config
        
        # Set each property of the json as an attribute
        for key, value in config.items():
            setattr(self, key, value)
        return config
    
    def set_config(self, config):
        self.config = config
        self.vals = config
        for key, value in config.items():
            setattr(self, key, value)
        return config

