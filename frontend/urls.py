from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='task-list'),
    path('tasks/<str:pk>/', views.detail, name='task-detail'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),
]