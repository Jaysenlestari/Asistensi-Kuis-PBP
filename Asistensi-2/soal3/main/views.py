from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST


@login_required
def dashboard(request):
    """TODO 1: hitung kunjungan dari session dan baca preferensi/cookie."""
    # raise NotImplementedError("TODO 1 belum dikerjakan")
    visit_count = request.session.get("visit_count", 0) + 1
    request.session["visit_count"] = visit_count
    context = {
        "visit_count": visit_count,
        "theme": request.session.get("theme", "light"),
        "announcement_dismissed": request.COOKIES.get("announcement_dismissed") == "1",
    }
    return render(request, "main/dashboard.html", context)

@login_required
@require_POST
def set_theme(request):
    """TODO 2: validasi light/dark dan simpan tema di session."""
    # raise NotImplementedError("TODO 2 belum dikerjakan")
    theme = request.POST.get("theme")
    if theme not in {"light", "dark"}:
        return HttpResponseBadRequest("Tema tidak valid")
    request.session["theme"] = theme
    return redirect("main:dashboard")

@login_required
@require_POST
def dismiss_announcement(request):
    """TODO 3: set cookie announcement_dismissed pada response redirect."""
    # raise NotImplementedError("TODO 3 belum dikerjakan")
    response = redirect("main:dashboard")
    response.set_cookie(
        "announcement_dismissed",
        "1",
        max_age=604800,
        httponly=True,
        samesite="Lax",
    )
    return response

@login_required
@require_POST
def reset_preferences(request):
    """TODO 4: hapus key preferensi dari session dan cookie dari browser."""
    # raise NotImplementedError("TODO 4 belum dikerjakan")
    request.session.pop("theme", None)
    request.session.pop("visit_count", None)
    response = redirect("main:dashboard")
    response.delete_cookie("announcement_dismissed")
    return response