from django.forms import ModelForm

from main.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description"]
