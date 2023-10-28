from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class EmailBackend(ModelBackend):
  def authenticate(self, request, username=None, password=None, **kwargs):
    UserModel = get_user_model()
    # print("Username:", UserModel.objects.all())  # Add this line for debugging
    try:
        user = UserModel.objects.get(email=username)
        print(user.password == password)
        if user.check_password(password):
            return user
    except UserModel.DoesNotExist:
        return None

