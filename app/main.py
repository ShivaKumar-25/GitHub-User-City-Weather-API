from fastapi import FastAPI, HTTPException
from app.github_api import fetch_github_user
from app.weather_api import get_weather
import logging


logging.basicConfig(
    filename="logs/api.log",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

app = FastAPI(title="GitHub & Weather API")


@app.get("/get_github_user")
def get_github_user(username: str):
    logger.info(f"Request received for GitHub user: {username}")
    try:
        return fetch_github_user(username)
    except HTTPException as e:
        logger.error(f"GitHub endpoint error: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error in GitHub endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/get_weather/{city}")
def get_weather_api(city: str):
    logger.info(f"Request received for weather: {city}")
    try:
        return get_weather(city)
    except HTTPException as e:
        logger.error(f"Weather endpoint error: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error in Weather endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))
