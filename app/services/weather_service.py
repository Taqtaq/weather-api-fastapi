from app.config import WEATHER_API_KEY
from fastapi import HTTPException
import requests
import time

cache = {}

def get_weather(city:str):
    current_time = time.time()
    if city in cache and current_time - cache[city]["time"] < 10:
        return cache[city]["data"]
    
    print("API CALL")
    response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?key={WEATHER_API_KEY}")
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="City not found")
    
    result = response.json()

    weather_data = {
        "city": result["resolvedAddress"],
        "temperature": result["days"][0]["temp"],
        "condition": result["days"][0]["conditions"]
    }
    cache[city] = {"data": weather_data,
                   "time": current_time }
    
    return cache[city]["data"]
