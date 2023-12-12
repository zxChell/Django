from django.shortcuts import render, redirect
from app1.forms import *
from django.http import HttpResponse

# Create your views here.


def log(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():

            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            if login == 'User1' and password == 12345678 and email == 'kekqurik@list.ru':
                return HttpResponse(f'Вы успешно вошли {login} {password} {email}')
            else:
                return redirect('register')

    else:
        form = UserForm()
        return render(request, 'login.html', context={'form': form})


def register(request):
    if request.method == "POST":
        form = UserFormTwo(request.POST)
        if form.is_valid():

            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            passwordTwo = form.cleaned_data['passwordTwo']
            email = form.cleaned_data['email']

            # if password == passwordTwo:

        return render(request, 'register.html')

    else:
        form = UserFormTwo()
        return render(request, 'register.html', context={'form': form})
