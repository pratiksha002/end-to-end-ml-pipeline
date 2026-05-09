import pandas as pd
import yaml
from src.utils.logger import logger

class DataValidation:
    def __init__(self, schema_path="config/schema.yaml"):
        self.schema_path = schema_path

    def read_schema(self):
        with open(self.schema_path, 'r') as file:
            schema = yaml.safe_load(file)
        return schema 
    
    def validate_columns(self, df: pd.DataFrame):
        try:
            logger.info("Data validation started.")
            schema = self.read_schema()
            expected_columns = schema["columns"]
            missing_columns = [
                col for col in expected_columns if col not in df.columns
            ]
            if missing_columns:
                raise ValueError(f"Missing columns:, {missing_columns}")
            
            extra_columns = [
                col for col in df.columns if col not in expected_columns
            ]

            if extra_columns:
                logger.warning(f"Extra columns found: {extra_columns}")

            logger.info("Column validation successful")
            return True
        
        except Exception as e:
            logger.error(f"Data validation failed: {e}")
            return e 