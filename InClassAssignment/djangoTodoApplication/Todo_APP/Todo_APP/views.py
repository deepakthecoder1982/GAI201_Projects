from rest_framework import viewsets
# from .serializer import todoSerializer
# from .models import TodoModel
from django.http import HttpResponse
# class TodoViewSet(viewsets.ModelViewSet):
#     queryset = TodoModel.objects.all()
#     # print(TodoModel.objects.all())
#     serializer_class = todoSerializer

def HomeViewSet(request):
    return HttpResponse("<h1>Welcome Home</h1>")