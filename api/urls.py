from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('tasks', views.TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include((router.urls, 'api'))),
]