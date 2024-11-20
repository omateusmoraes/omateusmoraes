from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # Renomeando a função login do Django
from django.contrib import messages
from .forms import LoginForm

from django.shortcuts import render

def user_login(request):  # Renomeando a função login para user_login
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('menu')  # Substitua 'menu' pela URL ou nome da view do menu
            else:
                messages.error(request, "Usuário ou senha incorretos")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def menu(request):
    return render(request, 'menu.html')
