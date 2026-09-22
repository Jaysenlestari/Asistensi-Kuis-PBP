from django.shortcuts import render
from main.models import Book


def book_list(request):
    return render(request, "main/book_list.html", {"books": Book.objects.all()})
