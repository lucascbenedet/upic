from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework import status
from .private import _login


@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    request.data['password'] = make_password(request.data.get('password'))
    serializer = UserSerializer(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error_messages)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not authenticate(username=username, password=password):
            raise ValidationError('Usuário ou senha inválidos')
        
        _login(username,password)

    
    except ValidationError as error:
        return Response(error.message,status=status.HTTP_400_BAD_REQUEST)
