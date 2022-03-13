
from todos.models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    """Todo model serializer class."""

    class Meta:
        model = Todo
        fields = ('id', 'detail', 'done', 'created_at')
        ordering = ('-created_at', )
