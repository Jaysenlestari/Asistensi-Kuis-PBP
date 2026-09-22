from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # TODO 1: teruskan seluruh URL proyek ke main.urls.
    path("", include("main.urls")),
]
