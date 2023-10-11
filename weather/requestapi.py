import os
import requests
import xmltodict
import json


def get_weather(city, country):

    api_key = os.environ.get('WEATHER_SECRET_APIKEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&mode=xml"

    response = requests.get(url)


    data_json = json.dumps(xmltodict.parse(response.content))
    current_data = json.loads(data_json)
    weather_data = current_data['current']


    location_name = f"{weather_data['city']['@name']}, {weather_data['city']['country']}"
    
    tempc = float(weather_data['temperature']['@value'])
    tempf = (tempc * (9/5)) + 32

    temperature_info = f"Температура в городе {location_name}: {tempc:.2f}°C, {tempf:.2f}°F"

    return temperature_info
