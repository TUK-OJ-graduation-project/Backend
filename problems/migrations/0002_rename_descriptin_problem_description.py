# Generated by Django 4.2 on 2023-04-09 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("problems", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="problem", old_name="descriptin", new_name="description",
        ),
    ]
