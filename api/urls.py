from django import views
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as rest_views

from todos.viewsets import TodoViewSet

router = routers.DefaultRouter()
router.register('todos', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token-auth', rest_views.obtain_auth_token)
]
