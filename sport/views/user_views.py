from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import django.contrib.auth as dj_auth

from sport.models import UserProfile
from sport.models import SignupForm
from sport.models import LoginForm


def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    elif request.method == "POST":
        f = SignupForm(request.POST)
        if f.is_valid():
            f.save()
            username = f.cleaned_data['username']
            new_user = User.objects.get(username=username)
            prof = UserProfile(user=new_user)
            prof.save()
            return redirect('login')
    else:
        f = SignupForm()
    return render(request, 'registration/signup.html', {'form': f})


def login(request):
    if request.user.is_authenticated:
        dj_auth.logout(request)
        return HttpResponseRedirect('/')
    elif request.method == "POST":
        f = LoginForm(data=request.POST)
        if f.is_valid():
            username = f.cleaned_data.get('username')
            password = f.cleaned_data.get('password')
            user = dj_auth.authenticate(username=username, password=password)
            if user is not None:
                dj_auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        f = LoginForm()
    return render(request, 'registration/login.html', {'form': f})
