from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import ObjectDoesNotExist
from django.contrib import messages
from .forms import TaskForm


@login_required
def list(request):
    return render(request, 'frontend/list.html')


@login_required
def detail(request, pk):
    return render(request, 'frontend/detail.html', context={'pk': pk, 'form': TaskForm})


def loginPage(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('task-list')

    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('task-list')
        else:
            messages.warning(request, "Invalid credentials")

    return render(request, 'frontend/login_register.html', context={'page_name': 'login'})


def registerPage(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('task-list')

    elif request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        try:
            User.objects.get(username=username)
            messages.warning(request, "User with this username already exists")
            return render(request, 'frontend/login_register.html', context={'page_name': 'register'})
        except ObjectDoesNotExist:
            pass

        if password1 == password2:
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            return redirect('task-list')
        else:
            messages.warning(request, "Passwords do not match")

    return render(request, 'frontend/login_register.html', context={'page_name': 'register'})

@login_required
def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')