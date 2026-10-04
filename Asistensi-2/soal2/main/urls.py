from django.contrib.auth import views as auth_views
from django.urls import path

from main.views import create_project, delete_project, edit_project, project_list, toggle_star

app_name = "main"

urlpatterns = [
    path("", project_list, name="project_list"),
    path("login/", auth_views.LoginView.as_view(template_name="main/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="main:project_list"), name="logout"),
    path("projects/create/", create_project, name="create_project"),
    path("projects/<int:project_id>/edit/", edit_project, name="edit_project"),
    path("projects/<int:project_id>/delete/", delete_project, name="delete_project"),
    path("projects/<int:project_id>/star/", toggle_star, name="toggle_star"),
]
