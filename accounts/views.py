from django.shortcuts import render
from rest_framework import status

from .serializers import UserRegisterSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response

# Create your views here.


class UserCreateApi(CreateAPIView):
    serializer_class = UserRegisterSerializer
    authentication_classes = ()
    permission_classes = ()


class LoginApi(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        return Response({'error': 'wrong credentials'}, status=status.HTTP_400_BAD_REQUEST)

