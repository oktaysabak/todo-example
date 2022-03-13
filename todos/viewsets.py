from rest_framework import viewsets
from todos.models import Todo
from todos.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    Todo viewset class to automatically provide list, create, retrieve,
    update and destroy actions.
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
