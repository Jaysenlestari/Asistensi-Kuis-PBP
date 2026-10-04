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
    # raise NotImplementedError("TODO 1 belum dikerjakan")
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:login")
    return render(request, "main/register.html", {"form": form})

def login_user(request):
    """TODO 2: autentikasi pengguna dan simpan cookie last_login."""
    # raise NotImplementedError("TODO 2 belum dikerjakan")
    form = AuthenticationForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        response = redirect("main:home")
        response.set_cookie("last_login", timezone.now().strftime("%Y-%m-%d %H:%M:%S"), max_age=3600, httponly=True, samsite="Lax")
        return response
    return render(request, "main/login.html", {"form": form})


def logout_user(request):
    """TODO 3: logout hanya melalui POST dan hapus cookie last_login."""
    # raise NotImplementedError("TODO 3 belum dikerjakan")
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    logout(request)
    response = redirect("main:home")
    response.delete_cookie("last_login")
    return response
