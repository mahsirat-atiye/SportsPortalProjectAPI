from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import django.contrib.auth as dj_auth

from api.email import send_email
from api.user import generate_hash, request_activation, validate_user
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
            email = f.cleaned_data['email']
            User.objects.filter(username=username).update(is_active=False)
            new_user = User.objects.get(username=username)
            prof = UserProfile(user=new_user)

            key = request_activation(username)

            send_email(email, 'activation', 'http://127.0.0.1:8000/validate/' + key)

            prof.save()
            return HttpResponseRedirect('/')
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


def validate(request, hashcode):
    validate_user(hashcode)
