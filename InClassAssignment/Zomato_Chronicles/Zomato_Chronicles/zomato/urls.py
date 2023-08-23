# zomato/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.display_menu, name='menu'),
    path('', views.display_page, name='dishes'),
    path('create/', views.add_dish, name='add_dish'),
     path('update/<int:dish_id>/', views.update_dish, name='update_dish'),
    # Add more URL patterns for other views as you progress
]
