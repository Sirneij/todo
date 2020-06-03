from rest_framework import generics
from . import models
from . import serializers


class TodoListAPIView(generics.ListAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer

class TodoDetailsAPIView(generics.RetrieveAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
