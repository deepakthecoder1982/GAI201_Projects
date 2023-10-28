from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Custom user model fields
    student_id = models.CharField(max_length=20, blank=True, null=True)
    major = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
     
    class Meta:
        permissions = [
            ("can_change_email", "Can change email address"),
            ("can_view_profile", "Can view user profile"),
            # Define other custom permissions here
        ]
    # Additional fields and methods as needed
User._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'