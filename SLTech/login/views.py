from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegUserForm


def loginU(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'Вы допустили ошибку')

    context = {}
    return render(request, 'login/log.html', context)


def logoutU(request):
    logout(request)
    return redirect('login')


def registerU(request):
    form = RegUserForm()

    if request.method == 'POST':
        form = RegUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')

    context = {'form': form}
    return render(request, 'login/reg.html', context)


@login_required(login_url='login')
def blog_main(request):
    return render(request, 'login/blog.html')
