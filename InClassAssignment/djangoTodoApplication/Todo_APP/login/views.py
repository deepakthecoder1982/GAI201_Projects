from django.contrib.auth import authenticate, login
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import loginSerilaizer, RegisterSerilaizer
from .models import Login, Registration

class LoginViewSet(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegisterSerilaizer
