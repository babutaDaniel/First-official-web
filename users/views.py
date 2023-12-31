from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
# Create your views here.

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user =authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("te-ai inregisrat cu succes"))
            return redirect('home')
    else:
        form= RegisterUserForm()
    return render(request, 'authenticate/register.html', {
        'form':form,
    })

def logout_user(request):
    logout(request)
    messages.success(request, ("You are out!"))
    return redirect('home')

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        #email = request.POST["email"]
        password = request.POST["password"]
        #confimPassword = request.POST["confirmPassword"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.success(request, ("Is a error"))
            return redirect('login')

    return render(request, 'authenticate/login.html', {})

