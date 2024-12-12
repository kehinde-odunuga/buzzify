from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class RegisterUserView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return Response({'error': 'All fields are required.'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        # if not username:
        #     return Response({'error': 'Username is required.'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        # if not email:
        #     return Response({'error': 'Email is required.'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already taken.'}, status=status.HTTP_409_CONFLICT)

        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({'id': user.id, 'username': user.username, 'email': user.email}, status=status.HTTP_201_CREATED)
