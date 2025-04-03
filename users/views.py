from django.contrib import auth
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrarionForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password= request.POST['password'] 
            user=auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
        
    context = {
        'title': ' Lilu – Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrarionForm(data=request.POST)
        if form.is_valid():
            form.save()
            user=form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrarionForm()

    context = {
        'title': ' Lilu – Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        'title': ' Lilu – Кабинет',
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))



