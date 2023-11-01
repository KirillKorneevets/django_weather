import os
import xmltodict
import json
import requests
from dotenv import load_dotenv
from datetime import datetime 


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
        'location': location_name,
        'temperature': f"Температура {tempc:.2f}°C",
        'humidity': f'Влажность: {humidity}%',
        'pressure': f'Давление: {pressure} hPa',
        'wind': f'Ветер: {wind_speed} м/с, {wind_direction}',
        'clouds': f'Облачность: {clouds}',
        'visibility': f'Видимость: {visibility} м',
    }                                        
    return weather_info



def get_weather_5_days(city, country):
    api_key = os.environ.get('WEATHER_SECRET_APIKEY')
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{country}&appid={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        location_data = data['city']
        location_name = f"{location_data['name']}, {location_data['country']}"

        weather_info_5_days = []

        # Переменная для отслеживания текущей даты
        current_date = None

        for forecast in data['list']:
            timestamp = forecast['dt']
            date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

            # Если дата изменилась, добавляем новую запись в список
            if date != current_date:
                temperature = forecast['main']['temp'] - 273.15
                humidity = forecast['main']['humidity']
                pressure = forecast['main']['pressure']
                wind_speed = forecast['wind']['speed']
                wind_direction = forecast['wind']['deg']
                clouds = forecast['clouds']['all']
                visibility = forecast.get('visibility', 0)

                weather_info = {
                    'date': date,
                    'temperature': f"Температура: {temperature:.2f}°C",
                    'humidity': f'Влажность: {humidity}%',
                    'pressure': f'Давление: {pressure} hPa',
                    'wind': f'Ветер: {wind_speed} м/с, направление {wind_direction}°',
                    'clouds': f'Облачность: {clouds}%',
                    'visibility': f'Видимость: {visibility} м',
                }
                weather_info_5_days.append(weather_info)

                # Обновляем текущую дату
                current_date = date

        return {
            'location_name': location_name,
            'weather_info_5_days': weather_info_5_days
        }
    else:
        return None


