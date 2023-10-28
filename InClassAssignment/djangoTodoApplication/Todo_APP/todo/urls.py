from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import TodoViewSet
router = routers.DefaultRouter()

router.register(r"todo",TodoViewSet)

urlpatterns = [
    path("", include(router.urls))
]
