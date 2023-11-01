from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import WeatherSerializer
from .requestapi import get_weather, get_weather_5_days

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def display_weather(request):
    serializer = WeatherSerializer(data=request.GET)
    if serializer.is_valid():
        country = serializer.validated_data['country']
        city = serializer.validated_data['city']
        weather_data = get_weather(city, country)


        return render(request, 'current_weather.html', {'weather_info': weather_data})


    return Response(serializer.errors, status=400)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def weather_detail_5_days(request):
    serializer = WeatherSerializer(data=request.GET)
    if serializer.is_valid():
        country = serializer.validated_data['country']
        city = serializer.validated_data['city']
        weather_data = get_weather_5_days(city, country)


        return render(request, 'five_day_forecast.html', {'weather_info': weather_data})

    return Response(serializer.errors, status=400)


@api_view(['GET'])
def home_page(request):
    return render(request, 'home_page.html')

@api_view(['GET'])
def weather_form(request):
    return render(request, 'weather_form.html')

@api_view(['GET'])
def weather_form_5_days(request):
    return render(request, 'weather_form_5_days.html')

