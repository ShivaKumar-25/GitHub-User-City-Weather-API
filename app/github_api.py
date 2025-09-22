import requests
from fastapi import HTTPException

def fetch_github_user(username: str):
    url = f"https://api.github.com/users/{username}"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 404:
            raise HTTPException(status_code=404, detail="User not found")
        elif resp.status_code == 403:
            raise HTTPException(status_code=429, detail="API rate limit exceeded")
        resp.raise_for_status()
        data = resp.json()
        return {
            "login": data.get("login"),
            "name": data.get("name"),
            "public_repos": data.get("public_repos"),
            "followers": data.get("followers"),
            "following": data.get("following")
        }
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
