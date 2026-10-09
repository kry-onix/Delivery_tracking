from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
m = joblib.load("delivery_model.pkl")

class D(BaseModel):
	distance: float
	traffic: int
	weather: int
	delivery_speed: float

@app.get("/health")
def health():
	return {"status": "ok"}

@app.post("/predict")
def predict(d: D):
	x = [[d.distance, d.traffic,
		d.weather, d.delivery_speed]]
	return {"delayed": int(m.predict(x)[0])}
