from fastapi import APIRouter
from app.schemas.weather import WeatherResponse

router = APIRouter()

@router.get("/weather/", response_model=WeatherResponse)
def weatherByCity(city:str):
    return {
    "city": city,
    "temperature": 25,
    "condition": "Sunny"
    }

