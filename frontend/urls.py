from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.list, name='task-list'),
    path('tasks/<str:pk>/', views.detail, name='task-detail'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)