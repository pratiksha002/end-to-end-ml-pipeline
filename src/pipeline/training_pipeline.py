from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_cleaning import DataCleaning
from src.components.data_transformation import (
    DataTransformation
)
from src.components.model_trainer import ModelTrainer
from src.utils.logger import logger


class TrainingPipeline:

    def __init__(self):

        logger.info(
            "Training Pipeline initialized"
        )

    def start_pipeline(self):

        try:

            logger.info(
                "Pipeline execution started"
            )

    
            ingestion = DataIngestion()
            df = ingestion.ingest_data()
            logger.info(
                "Data ingestion completed"
            )

           
            validation = DataValidation()
            validation.validate_columns(df)
            logger.info(
                "Data validation completed"
            )

            
            cleaning = DataCleaning()
            cleaned_df = cleaning.clean_data(df)
            logger.info(
                "Data cleaning completed"
            )

           
            transformation = DataTransformation()
            x_transformed, y = (
            transformation.transform_data(
            cleaned_df
            )
            )

            logger.info(
                "Data transformation completed"
            )

            logger.info(
                "Pipeline execution completed successfully"
            )

            trainer = ModelTrainer()
            metrics = trainer.train_model(x_transformed, y)
            logger.info(f"Training metrics: {metrics}")

            return x_transformed

        except Exception as e:

            logger.error(
                f"Pipeline failed: {e}"
            )

            raise e