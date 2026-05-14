from logging import config

import yaml
from src.entity.config_entity import DataIngestionConfig, DataCleaningConfig, DataTransformationConfig

class Configuration:
    def __init__(self, config_filepath="config/config.yaml"):
        with open(config_filepath, "r") as f:
            content = f.read()
            f.seek(0)
            self.config = yaml.safe_load(f)
            
    def get_data_ingestion_config(self):
        config = self.config["data_ingestion"]

        return  DataIngestionConfig(
            raw_data_path=config["raw_data_path"]
        )
    

    def get_data_cleaning_config(self):
        config = self.config["data_cleaning"]
        return DataCleaningConfig(
            remove_duplicates=config["remove_duplicates"],
            fill_missing=config["fill_missing"]
        )
    
    def get_data_transformation_config(self):

        config = self.config["data_transformation"]

        return DataTransformationConfig(
            scaling=config["scaling"],
            encoding=config["encoding"]
        )