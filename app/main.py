from fastapi import FastAPI
from app.routers.weather import router
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Weather API is running"}

app.include_router(router)