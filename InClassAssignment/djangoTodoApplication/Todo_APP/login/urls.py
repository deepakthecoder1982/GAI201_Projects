from django.urls import path, include
from rest_framework import routers
from .views import LoginViewSet, RegisterViewSet

router = routers.DefaultRouter()
# router.register(r"login", LoginViewSet)
router.register(r"register", RegisterViewSet)
# router.register(r"register", RegisterViewSet)

urlpatterns = [  # Corrected variable name
    path("", include(router.urls)),
    path("login/",LoginViewSet.as_view(),name="login")
]

# from django.urls import path
# from .views import LoginViewSet, RegisterViewSet

# urlpatterns = [
#     path("login/", LoginViewSet.as_view(), name="login"),  # Custom login view URL
#     path("register/", RegisterViewSet.as_view({'post': 'create'}), name="register"),  # Assuming 'create' maps to registration
# ]
