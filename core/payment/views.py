from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import re
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ValidationData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data
   
        username = data.get('username')
        if request.user.username != username:
            return Response({'error': 'Unauthorized user'}, status=status.HTTP_401_UNAUTHORIZED)
        
        email = data.get('email')
        if request.user.email != email:
            return Response({'error': 'Invalid email'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return Response({'error': 'Invalid email format '}, status=status.HTTP_400_BAD_REQUEST)
        
        card_number = data.get('cardNumber')
        if not re.match(r'^\d{16}$', card_number):
            return Response({'error': 'Invalid credit card number '}, status=status.HTTP_400_BAD_REQUEST)
        
        
        expiration = data.get('expiration')
        if not re.match(r'^(0[1-9]|1[0-2])\/\d{4}$', expiration):
            return Response({'error': 'Invalid expiration date (MM/YY)'}, status=status.HTTP_400_BAD_REQUEST)
        
        cvv = data.get('cvv')
        if not re.match(r'^\d{3,4}$', cvv):
            return Response({'error': 'invalid CVV'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'sucess': 'Valid data'}, status=status.HTTP_200_OK)
    
        
        