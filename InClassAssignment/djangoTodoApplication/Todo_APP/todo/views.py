# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializer import todoSerializer
from .models import TodoModel

class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoModel.objects.all()
    # print(TodoModel.objects.all())
    serializer_class = todoSerializer

