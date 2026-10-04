from django.urls import path

from main.views import home, login_user, logout_user, register

app_name = "main"

urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]
