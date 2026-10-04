from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    starred_by = models.ManyToManyField(User, blank=True, related_name="starred_projects")

    def __str__(self):
        return self.title
