# 🌦️ Weather App

A simple fullstack weather application built with FastAPI, Redis, and vanilla JavaScript.  
It fetches weather data from an external API and caches it using Redis.

---

## 🚀 Features

- Get current weather by city
- FastAPI backend
- Redis caching with TTL (10 seconds)
- Simple frontend (HTML, CSS, JavaScript)
- Error handling for invalid cities
- Loading state
- Clean UI

---

## 🛠 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/weather-app.git
cd weather-app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` file

Create a `.env` file in the root directory and add:

```env
WEATHER_API_KEY=your_api_key_here
```

Get your API key from:  
https://www.visualcrossing.com/

### 4. Run Redis with Docker

```bash
docker run --name weather-redis -p 6379:6379 -d redis
```

### 5. Run backend

```bash
python -m uvicorn app.main:app --reload
```

Backend will run at:

```text
http://127.0.0.1:8000
```

### 6. Run frontend

Open:

```text
frontend/index.html
```

Or use Live Server in VS Code.

---

## 📡 API

```text
GET /weather/?city=CityName
```

Example:

```text
http://127.0.0.1:8000/weather/?city=Tbilisi
```

---

## 🧪 Caching Logic

- First request → API CALL
- Next requests → served from Redis
- After 10 seconds → cache expires → new API CALL

---

## 🔧 Technologies

- FastAPI
- Redis
- Docker
- JavaScript (Fetch API)
- HTML
- CSS
- Visual Crossing Weather API

---

## 📂 Project Structure

```text
app/
├── routers/
├── services/
├── schemas/
├── config.py
├── main.py

frontend/
├── index.html
├── style.css
├── script.js

requirements.txt
```

---


## 💡 Notes

This project demonstrates:

- Working with third-party APIs
- Caching with Redis
- Building a simple fullstack app
---

https://roadmap.sh/projects/weather-api-wrapper-service

## 🌐 Live Demo

Frontend: https://taqtaq.github.io/weather-api-fastapi/  
Backend: https://weather-api-fastapi-9qzk.onrender.com

## 👨‍💻 Author

Nika Taqtaqishvili (Taqtaq)  

---

## 📬 Contact

If you have any questions, feel free to reach out:  
Telegram: https://t.me/nik_tqtq
Email: nikataqtaqishvili72@gmail.com
