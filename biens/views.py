# biens/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Bien

def index(request):
    biens = Bien.objects.all()
    return render(request, 'biens/index.html', {'biens': biens})

def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige vers l'index après connexion
    else:
        form = AuthenticationForm()
    return render(request, 'biens/connexion.html', {'form': form})

def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = UserCreationForm()
    return render(request, 'biens/inscription.html', {'form': form})

def deconnexion(request):
    logout(request)  # Déconnexion de l'utilisateur
    return redirect('index')  # Redirige vers l'index après déconnexion