import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


model = joblib.load("artifacts/model.pkl")
preprocessor = joblib.load("artifacts/preprocessor.pkl")


app = FastAPI()


class PredictionInput(BaseModel):

    age: int
    department: str
    experience: int


# Root endpoint
@app.get("/")
def home():
    return {"message": "ML Pipeline API Running"}

# Prediction endpoint
@app.post("/predict")
def predict(data: PredictionInput):
    input_df = pd.DataFrame([{
        "age": data.age,
        "department": data.department,
        "experience": data.experience
    }])

    transformed_input = (preprocessor.transform(input_df))

    # Predict
    prediction = model.predict(transformed_input)

    return {"predicted_salary": float(prediction[0])}