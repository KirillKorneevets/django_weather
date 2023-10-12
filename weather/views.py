from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import WeatherSerializer
from .requestapi import get_weather

@api_view(['GET'])
def weather_detail(request):
    serializer = WeatherSerializer(data=request.GET)
    if serializer.is_valid():
        country = serializer.validated_data['country']
        city = serializer.validated_data['city']
        weather_data = get_weather(city, country)

        return Response({'temperature_info': weather_data})

    return Response(serializer.errors, status=400)
