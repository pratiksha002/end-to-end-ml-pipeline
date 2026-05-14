import yaml
from src.entity.config_entity import DataIngestionConfig

class Configuration:
    def __init__(self, config_filepath="config/config.yaml"):
        with open(config_filepath, "r") as f:
            content = f.read()

            print("FILE CONTENT:")
            print(content)

            f.seek(0)

            self.config = yaml.safe_load(f)

            print("PARSED YAML:")
            
    def get_data_ingestion_config(self):
        config = self.config["data_ingestion"]

        return  DataIngestionConfig(
            raw_data_path=config["raw_data_path"]
        )