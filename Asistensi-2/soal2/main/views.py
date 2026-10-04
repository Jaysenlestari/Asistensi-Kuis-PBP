from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from main.forms import ProjectForm
from main.models import Project


def has_role(user, role_name):
    return user.groups.filter(name=role_name).exists()


def project_list(request):
    projects = Project.objects.all()
    return render(
        request,
        "main/project_list.html",
        {
            "projects": projects,
            "is_editor": has_role(request.user, "Editor"),
            "is_owner": has_role(request.user, "Owner"),
        },
    )


@login_required
def create_project(request):
    """TODO 1: hanya anggota Owner; GET/POST ProjectForm; selainnya HTTP 403."""
    raise NotImplementedError("TODO 1 belum dikerjakan")


@login_required
def edit_project(request, project_id):
    """TODO 2: hanya anggota Owner atau Editor; GET/POST ProjectForm."""
    raise NotImplementedError("TODO 2 belum dikerjakan")


@login_required
@require_POST
def delete_project(request, project_id):
    """TODO 3: hanya anggota Owner; hapus objek lalu redirect."""
    raise NotImplementedError("TODO 3 belum dikerjakan")


@login_required
@require_POST
def toggle_star(request, project_id):
    """TODO 4: tambah/hapus request.user pada relasi starred_by."""
    raise NotImplementedError("TODO 4 belum dikerjakan")
