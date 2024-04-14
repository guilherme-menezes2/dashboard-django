from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login para acessar a dashboard')
        return redirect('login')
    
    return render(request, 'dashboard/index.html')

def tempo(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    return render(request, 'dashboard/tempo.html')
