from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import RegUserForm

def login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
# Добавить страницу аккаунта
        if user is not None:
            login(request, username)
            redirect('')

    context = {}
    return render(request, 'main/log.html')



def register(request):
    form = RegUserForm()

    if request.method == 'POST':
        form = RegUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login', )

    context = {'form': form}
    return render(request, 'main/reg.html', context)


def blog_main(request):
    pass