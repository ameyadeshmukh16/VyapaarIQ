
from fastapi import FastAPI
from forecasting import forecast_sales
from bedrock_client import generate_insight

app = FastAPI()

@app.post("/forecast")
def forecast(data: dict):
    prediction = forecast_sales(data["sales"])
    insight = generate_insight(prediction)
    return {"forecast": prediction, "ai_insight": insight}
