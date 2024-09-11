from fastapi import FastAPI
from pydantic import BaseModel
from model import get_model, predict

app = FastAPI()

# load the model
model = get_model()

class WineRequest(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

@app.post("/predict/")
async def predict_wine_quality(wine: WineRequest):
    features = [
        wine.fixed_acidity, wine.volatile_acidity, wine.citric_acid, 
        wine.residual_sugar, wine.chlorides, wine.free_sulfur_dioxide, 
        wine.total_sulfur_dioxide, wine.density, wine.pH, 
        wine.sulphates, wine.alcohol
    ]
    
    # prediction making
    prediction = predict(model, features)
    
    # predicted quality retrning as a float
    return {"predicted_quality": float(prediction[0])}