from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Other URLs
    path('register/instructor/', views.instructor_registration, name='instructor_registration'),
    path('register/student/', views.student_registration, name='student_registration'),
]