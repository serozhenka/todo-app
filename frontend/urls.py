from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='task-list'),
    path('<str:pk>/', views.detail, name='task-detail'),
]