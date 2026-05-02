from app.config import WEATHER_API_KEY
from fastapi import HTTPException
import requests
import redis
import json
r = redis.Redis(host='localhost', port=6379, decode_responses=True)


def get_weather(city:str):
    if r.get(city):
        return json.loads(r.get(city))
    
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
    r.set(city, json.dumps(weather_data), ex=10)
    
    return json.loads(r.get(city))
