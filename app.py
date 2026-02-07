from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

app = FastAPI(
    title="Soil Fertility Classifier",
    version="1.0.0"
)

# Load trained model
model = pickle.load(open("model/rf_model.pkl", "rb"))

# Input schema (MATCHES TRAINING FEATURES)
class SoilInput(BaseModel):
    N: float
    P: float
    K: float
    ph: float
    ec: float
    oc: float
    S: float
    zn: float
    fe: float
    cu: float
    Mn: float
    B: float

@app.get("/")
def root():
    return {"message": "Soil Fertility Classifier API is running"}

@app.post("/predict")
def predict(data: SoilInput):
    try:
        # Feature order MUST match training
        features = np.array([
            data.N,
            data.P,
            data.K,
            data.ph,
            data.ec,
            data.oc,
            data.S,
            data.zn,
            data.fe,
            data.cu,
            data.Mn,
            data.B
        ]).reshape(1, -1)

        proba = model.predict_proba(features)[0]

        return {
    "soil_fertility": "Fertile" if proba[1] >= 0.5 else "Not Fertile",
    "fertility_probability": round(float(proba[1]), 3)
}


    except Exception as e:
        return {"error": str(e)}
