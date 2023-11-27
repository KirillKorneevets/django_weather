from rest_framework.response import Response
from django.db import IntegrityError
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
from django.urls import reverse
from django.http import HttpResponseRedirect


class UserRegistrationView(APIView):
    def get(self, request):
        return render(request, 'create_user.html')
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)

                response = redirect('weather:home-page')
                response.set_cookie('access_token', access_token)
                response.set_cookie('refresh_token', refresh_token)
                return response
            
            except IntegrityError:
                return Response({'message': 'Username already exists'}, status=400)
        return Response(serializer.errors, status=400)
    

class UserLoginView(APIView):
    def get(self, request):
        return render(request, 'login_user.html')
    
    def post(self, request):
            username = request.data.get('username')
            password = request.data.get('password')
            user = User.objects.get(username=username, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)

                response = redirect('weather:home-page')
                response.set_cookie('access_token', access_token)
                response.set_cookie('refresh_token', refresh_token)
                return response
            else:
                raise AuthenticationFailed({'message': 'Wrong login or password'})


@api_view(['GET'])
def main_page(request):
    return render(request, 'main.html')
    
