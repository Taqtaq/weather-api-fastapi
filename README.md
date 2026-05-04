🌦️ Weather App

A simple fullstack weather application built with FastAPI, Redis, and
vanilla JavaScript. It fetches weather data from an external API and
caches it using Redis.

------------------------------------------------------------------------

🚀 Features

-   Get current weather by city
-   FastAPI backend
-   Redis caching with TTL (10 seconds)
-   Simple frontend (HTML, CSS, JavaScript)
-   Error handling (invalid city)
-   Loading state
-   Clean UI

------------------------------------------------------------------------

🛠 How to Run

1.  Clone the repository: git clone
    https://github.com/YOUR_USERNAME/weather-app.git cd weather-app

2.  Install dependencies: pip install -r requirements.txt

3.  Create .env file: WEATHER_API_KEY=your_api_key_here

Get your API key from: https://www.visualcrossing.com/

4.  Run Redis (Docker): docker run –name weather-redis -p 6379:6379 -d
    redis

5.  Run backend: python -m uvicorn app.main:app –reload

6.  Run frontend: Open frontend/index.html or use Live Server in VS
    Code.

------------------------------------------------------------------------

📡 API

GET /weather/?city=CityName

Example: http://127.0.0.1:8000/weather/?city=Tbilisi

------------------------------------------------------------------------

🧪 Caching Logic

-   First request → API CALL
-   Next requests → served from Redis
-   After 10 seconds → cache expires → new API CALL

------------------------------------------------------------------------

🔧 Technologies

-   FastAPI
-   Redis
-   Docker
-   JavaScript (Fetch API)
-   HTML / CSS
-   Visual Crossing Weather API

------------------------------------------------------------------------

📂 Project Structure

app/ routers/ services/ schemas/ config.py main.py

frontend/ index.html style.css script.js

requirements.txt

------------------------------------------------------------------------

💡 Notes

This project demonstrates: - working with third-party APIs - caching
with Redis - building a simple fullstack app

------------------------------------------------------------------------

👨‍💻 Author

Nika Taqtaqishvili
------------------------------------------------------------------------

📬 Contact

If you have any questions, feel free to reach out: https://t.me/nik_tqtq
