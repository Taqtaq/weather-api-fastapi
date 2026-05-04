from app.config import WEATHER_API_KEY, REDIS_HOST, REDIS_PORT
from fastapi import HTTPException
import requests
import redis
import json

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


def get_weather(city:str):
    city_in_cache = r.get(city)
    if city_in_cache:
        return json.loads(city_in_cache)
    
    print("API CALL")
    response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?key={WEATHER_API_KEY}")
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="City not found")
    
    result = response.json()

    temp_f = result["days"][0]["temp"]
    temp_c = (temp_f - 32) * 5 / 9

    weather_data = {
        "city": result["resolvedAddress"],
        "temperature": round(temp_c,1),
        "condition": result["days"][0]["conditions"]
    }
    r.set(city, json.dumps(weather_data), ex=10)
    
    return weather_data
