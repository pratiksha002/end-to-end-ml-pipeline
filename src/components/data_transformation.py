import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler
)
from src.utils.logger import logger
from src.config.configuration import Configuration
import os
import joblib

class DataTransformation:

    def __init__(self):

        self.config = (
            Configuration()
            .get_data_transformation_config()
        )

    def transform_data(self, df: pd.DataFrame):

        try:

            logger.info("Data transformation started")

            # Separate column types
            categorical_columns = df.select_dtypes(
                include=['object']
            ).columns

            numerical_columns = df.select_dtypes(
                include=['number']
            ).columns

            logger.info(
                f"Categorical columns: {list(categorical_columns)}"
            )

            logger.info(
                f"Numerical columns: {list(numerical_columns)}"
            )

            # Numerical pipeline
            num_pipeline = Pipeline([
                ('scaler', StandardScaler())
            ])

            # Categorical pipeline
            cat_pipeline = Pipeline([
                ('encoder', OneHotEncoder(
                    handle_unknown='ignore'
                ))
            ])

            # Combine pipelines
            preprocessor = ColumnTransformer([

                ('num', num_pipeline, numerical_columns),

                ('cat', cat_pipeline, categorical_columns)

            ])

            
            os.makedirs("artifacts", exist_ok=True)

            # Transform data
            transformed_data = preprocessor.fit_transform(df)

            # Save transformed data
            joblib.dump(
                transformed_data,
                "artifacts/transformed_data.pkl"
            )

            # Save preprocessor object
            joblib.dump(
                preprocessor,
                "artifacts/preprocessor.pkl"
            )

            logger.info(
                "Transformation artifacts saved successfully"
            )

            logger.info(
                "Data transformation completed successfully"
            )

            return transformed_data

        except Exception as e:

            logger.error(
                f"Error during transformation: {e}"
            )
            raise e