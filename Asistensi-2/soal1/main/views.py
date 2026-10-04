from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.utils import timezone


def home(request):
    return render(
        request,
        "main/home.html",
        {"last_login": request.COOKIES.get("last_login")},
    )


def register(request):
    """TODO 1: proses UserCreationForm untuk GET dan POST."""
    raise NotImplementedError("TODO 1 belum dikerjakan")


def login_user(request):
    """TODO 2: autentikasi pengguna dan simpan cookie last_login."""
    raise NotImplementedError("TODO 2 belum dikerjakan")


def logout_user(request):
    """TODO 3: logout hanya melalui POST dan hapus cookie last_login."""
    raise NotImplementedError("TODO 3 belum dikerjakan")
