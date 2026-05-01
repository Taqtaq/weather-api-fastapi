from app.config import WEATHER_API_KEY
from fastapi import HTTPException
import requests

def get_weather(city:str):
    print("API CALL")
    response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?key={WEATHER_API_KEY}")
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="City not found")
    
    result = response.json()
    
    return {
        "city": result["resolvedAddress"],
        "temperature": result["days"][0]["temp"],
        "condition": result["days"][0]["conditions"]
    }
