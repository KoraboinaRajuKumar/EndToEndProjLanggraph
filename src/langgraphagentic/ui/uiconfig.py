from configparser import ConfigParser

class Config:
    def __init__(self,config_file="./src/langgraphagentic/ui/uiconfigfile.ini"):
        self.config=ConfigParser()
        self.config.read(config_file)
