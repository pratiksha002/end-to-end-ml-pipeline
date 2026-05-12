from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation

if __name__ == "__main__":

    ingestion = DataIngestion()
    df = ingestion.ingest_data()

    validation = DataValidation()
    validation.validate_columns(df)

    print("Validation successful")