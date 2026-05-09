import os
import pandas as pd

from src.utils.logger import logger
from src.config.configuration import Configuration

class DataIngestion:
    def __init__(self):
        self.config = Configuration().get_data_ingestion_config()

    def ingest_data(self):
        try:
            logger.info("Data ingestion started")

            data_path = self.config.raw_data_path
            logger.info(f"Reading data from: {data_path}")

            if not os.path.exists(data_path):
                raise FileNotFoundError(f"Data file not found at path: {data_path}")
            
            df = pd.read_csv(data_path)

            logger.info(f"Data loaded successfully with shape: {df.shape}")
            return df
        
        except Exception as e:
            logger.error(f"Error during data ingestion: {e}")

            raise e