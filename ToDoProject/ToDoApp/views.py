from django.shortcuts import render
from .serializers import Todo,ToDoSerializer
from rest_framework import viewsets

# Create your views here.
class TodoView(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = Todo.objects.all()
