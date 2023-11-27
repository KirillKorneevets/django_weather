import os
import requests
from dotenv import load_dotenv
from datetime import datetime 


load_dotenv()



def get_weather(city, country):
    api_key = os.environ.get('WEATHER_SECRET_APIKEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}"

    response = requests.get(url)

    if response.status_code != 200:
        return {'error': 'Failed to fetch weather data.'}

    try:
        data = response.json()

        location_name = f"{data.get('name', '')}, {data.get('sys', {}).get('country', '')}"

        tempk = float(data.get('main', {}).get('temp', 0))
        tempc = tempk - 273.15

        humidity = int(data.get('main', {}).get('humidity', 0))
        pressure = int(data.get('main', {}).get('pressure', 0))
        wind_speed = float(data.get('wind', {}).get('speed', 0))
        
        wind_direction = data.get('wind', {}).get('deg', '')

        clouds = data.get('clouds', {}).get('all', '')
        visibility = int(data.get('visibility', 0))

        weather_info = {
            'location': location_name,
            'temperature': f"Температура {tempc:.2f}°C",
            'humidity': f'Влажность: {humidity}%',
            'pressure': f'Давление: {pressure} hPa',
            'wind': f'Ветер: {wind_speed} м/с, направление {wind_direction}°',
            'clouds': f'Облачность: {clouds}%',
            'visibility': f'Видимость: {visibility} м',
        }
        return weather_info

    except Exception as e:
        return {'error': f'An error occurred: {str(e)}'}




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


