from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout as userlogout,login as userlogin
from django.contrib import messages
from django.contrib.auth.hashers import make_password




# Create your views here.


def index(request):
    return render(request, 'index.html')

def registration_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password: 
            user = User(username=username, email=email, password=make_password(password))
            user.save()
            messages.add_message(request, messages.SUCCESS, "You have successfully registered!")
            return redirect(login)
    return render(request,'registration/registration_form.html',)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            userlogin(request, user)
            messages.add_message(request, messages.SUCCESS, "You have successfully login!")
            return redirect('index')
        else:
            messages.add_message(request, messages.WARNING, "Invalid credentials!")
            return redirect('login')
    else:
        return render(request,'registration/login.html',)