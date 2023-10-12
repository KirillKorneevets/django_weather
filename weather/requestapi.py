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
    temperature_info = f"Температура в городе {location_name}: {tempc:.2f}°C"

    return temperature_info
