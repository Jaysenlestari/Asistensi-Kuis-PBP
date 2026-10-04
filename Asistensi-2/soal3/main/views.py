from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST


@login_required
def dashboard(request):
    """TODO 1: hitung kunjungan dari session dan baca preferensi/cookie."""
    raise NotImplementedError("TODO 1 belum dikerjakan")


@login_required
@require_POST
def set_theme(request):
    """TODO 2: validasi light/dark dan simpan tema di session."""
    raise NotImplementedError("TODO 2 belum dikerjakan")


@login_required
@require_POST
def dismiss_announcement(request):
    """TODO 3: set cookie announcement_dismissed pada response redirect."""
    raise NotImplementedError("TODO 3 belum dikerjakan")


@login_required
@require_POST
def reset_preferences(request):
    """TODO 4: hapus key preferensi dari session dan cookie dari browser."""
    raise NotImplementedError("TODO 4 belum dikerjakan")
