from django.contrib.auth import get_user_model,login
from django.contrib.auth.models import update_last_login
from django.contrib.auth.backends import BaseBackend
from django.utils import timezone
from django.contrib.auth.hashers import check_password
from .models import Registration

class CustomAuthenticationBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            registration = Registration.objects.get(email=email)
            if registration.password == password:
                # registration.last_login = None  # Set last_login to None
                login(request, registration)  # Log in the user without updating last_login
                # print("Login successful")
                return registration  # Authentication success
        except Registration.DoesNotExist:
            pass  # User doesn't exist
        return None  # Authentication failed

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        
    # def update_last_login(self, request, user):
    #     """
    #     Update the user's last_login timestamp when they log in.
    #     """
    #     user.last_login = timezone.now()
    #     user.save(update_fields=['last_login'])
