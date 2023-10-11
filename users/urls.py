from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.authenticate_user),
    path("create/", views.create_user),
]

