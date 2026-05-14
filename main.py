from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_cleaning import DataCleaning
from src.components.data_transformation import DataTransformation

if __name__ == "__main__":

    ingestion = DataIngestion()
    df = ingestion.ingest_data()

    validation = DataValidation()
    validation.validate_columns(df)

    cleaning = DataCleaning()
    cleaned_df = cleaning.clean_data(df)

    transformation = DataTransformation()
    transformed_data = (transformation.transform_data(cleaned_df))

    print(transformed_data)