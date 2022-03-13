
from todos.models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    """Todo model serializer class."""

    class Meta:
        model = Todo
        fields = ('id', 'detail', 'done', 'created_at')
        ordering = ('-created_at', )

    def to_representation(self, instance):
        """
        Representation method for todo object serializer.

        Args:
            instance(obj): Todo object instance.

        Returns:
            json: Serialized todo item.

        """
        data = super(TodoSerializer, self).to_representation(instance)
        data.pop('created_at')
        return data
