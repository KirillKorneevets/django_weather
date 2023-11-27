from django.urls import path
from .views import UserRegistrationView, UserLoginView, main_page
from . import views

urlpatterns = [
    path("login/", UserLoginView.as_view(), name='login'),
    path("create/", UserRegistrationView.as_view(), name='create'),
    path("", views.main_page, name='main_page'),

]

