import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import IntegrityError
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
import secrets
import string
from .models import User, UserToken

def generate_unique_token():
    generation = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(generation) for _ in range(40))
    return token



@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                token = generate_unique_token()
                UserToken.objects.create(user=user, token=token)

                return Response({'message': 'User created successfully', 'token': token}, status=201)
            except IntegrityError:
                return Response({'message': 'Username already exists'}, status=400)
        return Response(serializer.errors, status=400)
    

@api_view(['POST'])
def authenticate_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username', '')
        password = data.get('password', '')
        
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            user = None
        
        if user is not None:
            token, _ = UserToken.objects.get_or_create(user=user)
            return Response({'message': 'Authentication successful', 'token': token.token})
        else:
            return Response({'message': 'Wrong login or password'}, status=401)
    else:
        return Response({'message': 'Invalid request method'}, status=400)
