from django.shortcuts import render

from main.models import Book


def book_list(request):
    # TODO 2: ambil seluruh Book dan kirimkan ke template dengan key "books".
    return render(request, "main/book_list.html", {})
