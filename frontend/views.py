from django.shortcuts import render
from .forms import TaskForm

def list(request):
    return render(request, 'frontend/list.html')

def detail(request, pk):
    return render(request, 'frontend/detail.html', context={'pk': pk, 'form': TaskForm})
