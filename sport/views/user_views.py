from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
import django.contrib.auth as dj_auth

from api.email import send_email
from api.user import generate_hash, request_activation, activation_check, forgotten_check, request_forgotten
from react_django import settings
from sport.models import UserProfile, ForgottenUser
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

            send_email(email, 'activation', 'http://127.0.0.1:8000/' + key + '/activate/')

            prof.save()
            return HttpResponseRedirect('/')
    else:
        f = SignupForm()
    return render(request, 'registration/signup.html', {'form': f})


def login(request):
    if request.user.is_authenticated:
        dj_auth.logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)
        # return HttpResponse("cici")
    elif request.method == "POST":
        f = LoginForm(data=request.POST)
        if f.is_valid():
            username = f.cleaned_data.get('username')
            password = f.cleaned_data.get('password')
            user = dj_auth.authenticate(username=username, password=password)
            if user is not None:
                dj_auth.login(request, user)
                return HttpResponseRedirect(settings.REDIRECT_URL)
                # return HttpResponse("hihi")
    else:
        f = LoginForm()
    return render(request, 'registration/login.html', {'form': f})
    # return HttpResponse("bibi")


def reset_request(request):
    if request.user.is_authenticated:
        dj_auth.logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)
    elif request.method == "POST":
        email = request.POST.get('email', '')
        if email:
            try:
                username = User.objects.filter(email=email)[0].username

                key = request_forgotten(username)
                send_email(email, 'forgotten', 'http://127.0.0.1:8000/' + key + '/reset/')

                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
            except IndexError:
                pass

    return render(request, 'registration/reset.html', {})


def activate(request, hashcode):
    if request.user.is_authenticated:
        dj_auth.logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)

    activation_check(hashcode)
    return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)


def reset(request, hashcode):
    if request.user.is_authenticated:
        dj_auth.logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)

    username = forgotten_check(hashcode)
    if username:
        if request.method == "POST":
            p1 = request.POST.get('password', '')
            p2 = request.POST.get('password_r', '')
            if p1 and p2 and p1 == p2:
                user = User.objects.filter(username=username)[0]
                user.set_password(p1)
                user.save()
                ForgottenUser.objects.filter(key=hashcode)[0].delete()
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    else:
        return HttpResponseRedirect(settings.REDIRECT_URL)

    return render(request, 'registration/change.html', {})
