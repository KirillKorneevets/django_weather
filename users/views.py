import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import IntegrityError
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken



@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)
                return Response({'message': 'User created successfully', 'access_token': access_token, 'refresh_token': refresh_token})
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
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({'message': 'Authentication successful', 'access_token': access_token})
        else:
            return Response({'message': 'Wrong login or password'}, status=401)
    else:
        return Response({'message': 'Invalid request method'}, status=400)