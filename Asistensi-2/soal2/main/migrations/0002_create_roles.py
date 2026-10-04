from django.db import migrations


def create_roles(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.get_or_create(name="Editor")
    Group.objects.get_or_create(name="Owner")


def remove_roles(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name__in=["Editor", "Owner"]).delete()


class Migration(migrations.Migration):
    dependencies = [("main", "0001_initial")]
    operations = [migrations.RunPython(create_roles, remove_roles)]
