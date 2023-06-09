from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse

from .forms import LoginForm

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("polls:index"))
            else:
                messages.success(request, "Username and/or password don't match. Try again.")
                return render(request, 'authenticate/login.html', {"form": LoginForm()})
    else:
        return render(request, 'authenticate/login.html', {"form": LoginForm()})
