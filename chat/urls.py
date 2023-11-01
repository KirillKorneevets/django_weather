from django.urls import path
from . import views


urlpatterns = [
    path("chat_html/<str:chat_id>/", views.ChatView.as_view(), name="chat_view"),
    path("start_chat/", views.StartChat.as_view(), name="start_chat"),

]

