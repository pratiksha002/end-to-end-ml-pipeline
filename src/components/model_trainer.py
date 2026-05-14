import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from src.utils.logger import logger

class ModelTrainer:
    def __init__(self):
        os.makedirs(
            "artifacts",
            exist_ok=True
        )

    def train_model(self, transformed_data):
        try:
            logger.info("Model training started")

            # Features and target
            x = transformed_data[:, :-1]

            y = transformed_data[:, -1]

            # Train-test split
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

            logger.info(
                "Train-test split completed"
            )

            # Create model
            model = LinearRegression()

            # Train model
            model.fit(x_train, y_train)

            logger.info(
                "Model training completed"
            )

            # Predictions
            y_pred = model.predict(x_test)

            # Metrics
            mae = mean_absolute_error(
                y_test,
                y_pred
            )

            mse = mean_squared_error(
                y_test,
                y_pred
            )

            r2 = r2_score(
                y_test,
                y_pred
            )

            logger.info(
                f"MAE: {mae}"
            )

            logger.info(
                f"MSE: {mse}"
            )

            logger.info(
                f"R2 Score: {r2}"
            )

            # Save model
            joblib.dump(
                model,
                "artifacts/model.pkl"
            )

            logger.info(
                "Model saved successfully"
            )

            return {
                "mae": mae,
                "mse": mse,
                "r2": r2
            }

        except Exception as e:

            logger.error(
                f"Model training failed: {e}"
            )

            raise e