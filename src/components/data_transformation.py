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

            # Separate features and target
            x = df.drop(columns=["salary"])

            y = df["salary"]

            # Detect column types
            categorical_columns = x.select_dtypes(
                include=['object']
            ).columns

            numerical_columns = x.select_dtypes(
                include=['number']
            ).columns

            logger.info(f"Categorical columns: {list(categorical_columns)}")

            logger.info(f"Numerical columns: {list(numerical_columns)}")

            # Numerical pipeline
            num_pipeline = Pipeline([('scaler', StandardScaler())])

            # Categorical pipeline
            cat_pipeline = Pipeline([('encoder', OneHotEncoder(handle_unknown='ignore'))])

            # Combine preprocessors
            preprocessor = ColumnTransformer([
                ('num', num_pipeline, numerical_columns),
                ('cat', cat_pipeline, categorical_columns)

            ])

            # Transform ONLY features
            X_transformed = (preprocessor.fit_transform(x))

            # Save preprocessor
            os.makedirs("artifacts",exist_ok=True)
            joblib.dump(preprocessor,"artifacts/preprocessor.pkl")
            logger.info("Transformation completed successfully")
            return X_transformed, y

        except Exception as e:
            logger.error(f"Transformation failed: {e}")
            raise e