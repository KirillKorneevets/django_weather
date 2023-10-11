from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=20)
    country = serializers.CharField(max_length=2)