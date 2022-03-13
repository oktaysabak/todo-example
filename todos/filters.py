from django_filters import rest_framework as filters

from todos.models import Todo


class TodoFilter(filters.FilterSet):
    """Filter class for filtering todos."""

    detail = filters.CharFilter(field_name='detail')
    done = filters.BooleanFilter(field_name='done')

    class Meta:
        model = Todo
        fields = ('detail', 'done')
