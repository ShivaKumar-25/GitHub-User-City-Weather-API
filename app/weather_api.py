import os
import requests
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city: str):
    if not api_key:
        raise HTTPException(status_code=500, detail="API key is missing.")
    
    # Get coordinates
    geo_url = "http://api.openweathermap.org/geo/1.0/direct"
    geo_params = {"q": city, "appid": api_key, "limit": 1}
    try:
        geo_resp = requests.get(geo_url, params=geo_params, timeout=10)
        geo_resp.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Geo API error: {e}")

    geo_data = geo_resp.json()
    if not geo_data:
        raise HTTPException(status_code=404, detail=f"Invalid city: {city}")

    lat, lon = geo_data[0]["lat"], geo_data[0]["lon"]

    # Get weather
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    weather_params = {"lat": lat, "lon": lon, "appid": api_key, "units": "metric"}
    try:
        weather_resp = requests.get(weather_url, params=weather_params, timeout=10)
        weather_resp.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Weather API error: {e}")

    w = weather_resp.json()
    return {
        "city": w.get("name"),
        "temperature": w.get("main", {}).get("temp"),
        "weather_description": w.get("weather", [{}])[0].get("description")
    }
