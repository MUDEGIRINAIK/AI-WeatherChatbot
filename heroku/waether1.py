import requests # type: ignore
from config import OPENWEATHER_API_KEY

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": OPENWEATHER_API_KEY, "units": "metric"}
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        icon = data['weather'][0]['icon']
        return {
            "city": city,
            "description": weather_desc,
            "temperature": temp,
            "icon": f"http://openweathermap.org/img/wn/{icon}.png"
        }
    else:
        return {"error": "City not found!"}
