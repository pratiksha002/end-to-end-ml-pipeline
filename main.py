from src.pipeline.training_pipeline import (
    TrainingPipeline
)


if __name__ == "__main__":

    pipeline = TrainingPipeline()

    transformed_data = (
        pipeline.start_pipeline()
    )

    print(transformed_data)