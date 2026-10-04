from django.contrib.auth import views as auth_views
from django.urls import path

from main.views import dashboard, dismiss_announcement, reset_preferences, set_theme

app_name = "main"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("login/", auth_views.LoginView.as_view(template_name="main/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="main:login"), name="logout"),
    path("preferences/theme/", set_theme, name="set_theme"),
    path("announcement/dismiss/", dismiss_announcement, name="dismiss_announcement"),
    path("preferences/reset/", reset_preferences, name="reset_preferences"),
]
