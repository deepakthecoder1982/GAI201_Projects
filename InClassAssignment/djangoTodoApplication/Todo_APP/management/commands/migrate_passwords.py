from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from login.models import Registration  # Replace with your actual user model

class Command(BaseCommand):
    help = 'Migrate plaintext passwords to hashed passwords'

    def handle(self, *args, **kwargs):
        for user in Registration.objects.all():
            user.password = make_password(user.password)
            user.save()
        self.stdout.write(self.style.SUCCESS('Password migration complete'))
