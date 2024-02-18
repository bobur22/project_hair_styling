from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import Registration, LoginForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ValidationError


def register_view(request):
    form = Registration()
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            del form.cleaned_data["confirm_password"]
            email = form.cleaned_data["email"]
            message = "You have registered your account."
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            send_mail(
                'Registration', message, 'settings.EMAIL_HOST_USER', [email], fail_silently=False)
            return redirect("login")

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    path_l = "/"
    # if request.method == "GET":
    #     path_l = request.GET.get("next", "")

    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = (authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']))

        if user is not None:
            login(request, user)
            return redirect(path_l)
        form.add_error("password", "Username yoki parol noto\'g\'ri ")
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")
