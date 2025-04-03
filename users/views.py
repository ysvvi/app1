from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories

def login(request):
    context = {
        'title': ' Lilu – Авторизация',
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': ' Lilu – Регистрация',
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        'title': ' Lilu – Кабинет',
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    ...



