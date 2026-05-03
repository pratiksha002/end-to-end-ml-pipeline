import yaml
from src.entity.config_entity import DataIngestionConfig

class Configuration:
    def __init__(self, config_filepath="config/config.yaml"):
        with open(config_filepath, "r") as f:
            self.config = yaml.safe_load(f)

    def get_data_ingestion_config(self):
        config = self.config["data_ingestion"]

        return  DataIngestionConfig(
            raw_data_path=config["raw_data_path"]
        )