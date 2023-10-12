import os
import requests
import xmltodict
import json
from dotenv import load_dotenv

load_dotenv()



def get_weather(city, country):

    api_key = os.environ.get('WEATHER_SECRET_APIKEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&mode=xml"

    response = requests.get(url)


    data_json = json.dumps(xmltodict.parse(response.content))
    current_data = json.loads(data_json)
    weather_data = current_data['current']


    location_name = f"{weather_data['city']['@name']}, {weather_data['city']['country']}"
    
    tempk = float(weather_data['temperature']['@value'])
    tempc = tempk - 273.15

    
    humidity = int(weather_data['humidity']['@value'])
    pressure = int(weather_data['pressure']['@value'])
    wind_speed = float(weather_data['wind']['speed']['@value'])
    wind_direction = weather_data['wind']['direction']['@name']
    clouds = weather_data['clouds']['@name']
    visibility = int(weather_data['visibility']['@value'])


    weather_info = {
        'temperature': f"Температура в городе {location_name}: {tempc:.2f}°C",
        'humidity': f'Влажность: {humidity}%',
        'pressure': f'Давление: {pressure} hPa',
        'wind': f'Ветер: {wind_speed} м/с, {wind_direction}',
        'clouds': f'Облачность: {clouds}',
        'visibility': f'Видимость: {visibility} м',
    }                                        
    return weather_info
