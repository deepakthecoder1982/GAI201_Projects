from django.db import models

# Create your models here.
class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    isSubscribed = models.BooleanField(default=False, choices=((False, 'Not Joined'), (True, 'Joined')))

class Login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    isSubscribed = models.BooleanField(default=False, choices=((False, 'Not Joined'), (True, 'Joined')))

   