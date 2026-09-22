from django.urls import path
from main.views import book_list

app_name = "main"
urlpatterns = [path("books/", book_list, name="book_list")]
