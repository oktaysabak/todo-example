from django.contrib import admin
from django.urls import include, path

from todos.views import TodoListView, TodoDetailView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/', include('api.urls'), name='api'),
    path('', TodoListView.as_view(), name='index'),
    path('detail/<int:pk>', TodoDetailView.as_view(), name='detail'),
]
