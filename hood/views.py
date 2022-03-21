from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout as userlogout,login as userlogin
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User




# Create your views here.

def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password = password)
            login(request, user)
            return redirect(index)
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})  
