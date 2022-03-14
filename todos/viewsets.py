from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, filters
from rest_framework.response import Response

from todos.filters import TodoFilter
from todos.models import Todo
from todos.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    View set class to automatically provide list, create, retrieve,
    update and destroy actions.
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ('content', )
    filterset_class = TodoFilter

    def get_queryset(self):
        """Get the list of items for this view set."""
        return self.request.user.todos.all().order_by('-created_at')
    
    def create(self, request, *args, **kwargs):
        """
        Create todo item method.

        Args:
            request(obj): Django request object.

        Returns:
            json: Requested todo item content.

        """
        todo_serializer = TodoSerializer(data=request.data)
        if todo_serializer.is_valid():
            Todo.objects.get_or_create(
                content=todo_serializer.validated_data.get('content'),
                done=todo_serializer.validated_data.get('done', False),
                owner=self.request.user
            )
        return Response(todo_serializer.validated_data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None, *args, **kwargs):
        """
        Retrieve requested todo item.

        Args:
            request(obj): Django request object.
            pk(int): unique primary key of todo item.

        Returns:
            json: Requested todo item content.

        """
        queryset = Todo.objects.filter(owner=self.request.user)
        todo = get_object_or_404(queryset, pk=pk)
        return Response(TodoSerializer(todo).data, status=status.HTTP_200_OK)

    def update(self, request, pk=None, *args, **kwargs):
        """
        Update method to update existing todo item.

        Args:
            request(obj): Django request object.
            pk(int): unique primary key of todo item.

        Returns:
            json: Requested todo item content.

        """
        queryset = Todo.objects.filter(owner=self.request.user)
        todo = get_object_or_404(queryset, pk=pk)
        todo_serializer = TodoSerializer(todo, data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save()

        return Response(todo_serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None, *args, **kwargs):
        """
        Destroy method to delete todo item.
        Args:
            request(obj): Django request object.
            pk(int): unique primary key of todo item.

        Returns:
            json: Requested todo item content.

        """
        queryset = Todo.objects.filter(owner=self.request.user)
        todo = get_object_or_404(queryset, pk=pk)
        todo.delete()
        return Response(TodoSerializer(todo).data, status=status.HTTP_204_NO_CONTENT)
