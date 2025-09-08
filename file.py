from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
import pandas as pd
import pickle

app = FastAPI()

with open("pipeline.pkl", "rb") as f:
    pipeline = pickle.load(f)

binary_map = {'yes': 1, 'no': 0, 'Male': 1, 'Female': 0}
ordinal_map = {'no': 0, 'Sometimes': 1, 'Frequently': 2, 'Always': 3}
binary_cols = ['family_history_with_overweight', 'FAVC', 'SMOKE', 'SCC', 'Gender']
ordinal_cols = ['CAEC', 'CALC']

class InputRow(BaseModel):
    Gender: str = Field(example="Female")
    Age: int = Field(example=22)
    Height: float = Field(example=1.65)
    Weight: float = Field(example=55.0)
    family_history_with_overweight: str = Field(example="yes")
    FAVC: str = Field(example="yes")
    FCVC: int = Field(example=3)
    NCP: int = Field(example=3)
    CAEC: str = Field(example="Sometimes")
    SMOKE: str = Field(example="no")
    CH2O: int = Field(example=2)
    SCC: str = Field(example="no")
    FAF: int = Field(example=1)
    TUE: int = Field(example=1)
    CALC: str = Field(example="no")
    MTRANS: str = Field(example="Public_Transportation")

def apply_mapping(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for col in binary_cols:
        df[col] = df[col].map(binary_map)
    for col in ordinal_cols:
        df[col] = df[col].map(ordinal_map)
    return df

@app.post("/predict")
def predict_obesity(data: List[InputRow]):
    df = pd.DataFrame([row.dict() for row in data])
    df = apply_mapping(df)
    predictions = pipeline.predict(df)
    return {"predictions": predictions.tolist()}
