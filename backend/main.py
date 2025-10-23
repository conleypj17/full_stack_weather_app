from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.weather_app_logic import fetch_weather
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Allow React frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/weather/{city}")
async def get_weather(city: str):
    data = await fetch_weather(city)
    logger = logging.getLogger("uvicorn")
    logger.info("hello world")

    return data