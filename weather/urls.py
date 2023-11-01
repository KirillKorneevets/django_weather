from django.urls import path
from . import views


urlpatterns = [
    path('current_weather/', views.display_weather, name='current_weather'),
    path("five_days_forecast/", views.weather_detail_5_days, name='five_days_forecast'),
    path("", views.home_page, name='home-page'),
    path("weather_form/", views.weather_form, name='weather_form'),
    path("weather_form_5_days/", views.weather_form_5_days, name='weather_form_5_days'),
]

