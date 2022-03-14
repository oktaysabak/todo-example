from django.views.generic import TemplateView


class TodoListView(TemplateView):
    """
    Todo list page view.
    """
    template_name = 'todos/list.html'

class TodoDetailView(TemplateView):
    """
    Todo detail page view.
    """
    template_name = 'todos/detail.html'
