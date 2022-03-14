from django_filters import rest_framework as filters

from todos.models import Todo


class TodoFilter(filters.FilterSet):
    """Filter class for filtering todos."""

    content = filters.CharFilter(field_name='content')
    done = filters.BooleanFilter(field_name='done')

    class Meta:
        model = Todo
        fields = ('content', 'done')
