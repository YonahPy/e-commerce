from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate, login
import re


class Register(APIView):
   def post(self, request):
       username = request.data.get('username')
       password = request.data.get('password')
       email = request.data.get('email')
       
       if not username or not password or not email:
           return Response({'error': 'Please provide username, password, and email'}, status=status.HTTP_400_BAD_REQUEST)
       
       if User.objects.filter(username=username).exists():
           return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
       
       if len(password) < 8 or not re.search("[0-9]", password) or not re.search("[!@#$^&*]", password):
           return Response({'error': 'Password must be at least 8 characters long, contain at least one number, and one special character'}, status=status.HTTP_400_BAD_REQUEST)
       
       if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
           return Response({'error': 'Invalid email format'}, status=status.HTTP_400_BAD_REQUEST)
       
       
       new_user = User.objects.create_user(username=username, password=password, email=email)
       new_user.save()
       
       token, created = Token.objects.get_or_create(user=new_user)
       
       return Response({'token': token.key}, status=status.HTTP_201_CREATED)
       
  
    
class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
    
class Logout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Logout sucessful'}, status=status.HTTP_200_OK)

 