import pandas as pd
from src.utils.logger import logger
from src.config.configuration import Configuration  

class DataCleaning:
    def __init__(self):
        self.config = Configuration().get_data_cleaning_config()

    def clean_data(self, df: pd.DataFrame):
        try:
            logger.info("Data cleaning started")
            
            if self.config.remove_duplicates:
                before = df.shape[0]
                df = df.drop_duplicates()
                after = df.shape[0]
                logger.info(f"Removed {before-after} duplicate rows")


            if self.config.fill_missing == "mean":
                numeric_cols = df.select_dtypes(include=['number']).columns

                for col in numeric_cols:
                    df[col] = df[col].fillna(df[col].mean())

                logger.info("Missing values filled using mean strategy")

            logger.info(f"Cleaned data shape: {df.shape}")

            return df
        
        except Exception as e:

            logger.error(f"Error during data cleaning: {e}")
            raise e
