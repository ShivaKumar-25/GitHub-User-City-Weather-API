# GitHub & Weather API

This project provides two HTTP GET endpoints:

1. `/get_github_user?username=:username`  
   Returns GitHub user details: login, name, public repos, followers, following.  

2. `/get_weather/:city`  
   Returns weather details for the given city: temperature (°C), weather description.

## Setup

git clone https://github.com/YourUsername/github_weather_api.git  
cd github_weather_api   
python -m venv venv   
venv\Scripts\activate   # Windows   
pip install -r requirements.txt   

Create `.env` file:   

OPENWEATHER_API_KEY=your_openweather_api_key_here   

## Run
 
uvicorn app.main:app --reload --port 3400   

## Usage Examples

- GitHub User:  
GET http://localhost:3400/get_github_user?username=octocat   

- Weather:  
GET http://localhost:3400/get_weather/London   

Logs are stored in `logs/api.log`.   
