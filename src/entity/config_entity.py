from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path: str

@dataclass
class DataCleaningConfig:
    remove_duplicates: bool
    fill_missing: str

@dataclass
class DataTransformationConfig:
    scaling: str
    encoding: str