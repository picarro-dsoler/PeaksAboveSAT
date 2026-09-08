class ETL:
    def __init__(self, config_file):
        self.config_file = config_file
        self.readConfigFile()

    def readConfigFile(self):
        with open(self.config_file, 'r') as file:
            config = json.load(file)
        return config
    
    def setLogger(self, logger):
        self.logger = logger
        return self
    
    def setConfig(self, config):
        self.config = config
        return self
    
    def setConfigFile(self, config_file):
        self.config_file = config_file
        return self 