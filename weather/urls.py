from django.urls import path
from . import views


urlpatterns = [
    path("get_weather/", views.weather_detail),
]

