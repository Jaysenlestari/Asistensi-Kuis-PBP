from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from main.forms import ProjectForm
from main.models import Project


def has_role(user, role_name):
    return user.groups.filter(name=role_name).exists()

def is_editor(user):
    return has_role(user, "Editor")

def is_owner(user):
    return has_role(user, "Owner")

def project_list(request):
    projects = Project.objects.prefetch_related("starred_by").all()
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
    # raise NotImplementedError("TODO 1 belum dikerjakan")
    if not (request.user.is_superuser or is_owner(request.user)):
        raise PermissionDenied
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:project_list")
    return render(request, "main/project_form.html", {"form": form, "heading": "Create Project"})


@login_required
def edit_project(request, project_id):
    """TODO 2: hanya anggota Owner atau Editor; GET/POST ProjectForm."""
    # raise NotImplementedError("TODO 2 belum dikerjakan")
    if not (is_owner(request.user) or is_editor(request.user)):
        raise PermissionDenied
    project = get_object_or_404(Project, id=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:project_list")
    return render(request, "main/project_form.html", {"form": form, "heading": "Edit Project"})

@login_required
@require_POST
def delete_project(request, project_id):
    """TODO 3: hanya anggota Owner; hapus objek lalu redirect."""
    # raise NotImplementedError("TODO 3 belum dikerjakan")
    if not (is_owner(request.user)):
        raise PermissionDenied
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect("main:project_list")

@login_required
@require_POST
def toggle_star(request, project_id):
    """TODO 4: tambah/hapus request.user pada relasi starred_by."""
    # raise NotImplementedError("TODO 4 belum dikerjakan")
    project = get_object_or_404(Project, id=project_id)
    if project.starred_by.filter(pk=request.user.pk).exists():
        project.starred_by.remove(request.user)
    else:
        project.starred_by.add(request.user)
    return redirect("main:project_list")