from fastapi import APIRouter

router = APIRouter()

@router.get("/weather/")
def weatherByCity(city:str=None):
    return {
    "city": city,
    "temperature": 25,
    "condition": "Sunny"
    }

