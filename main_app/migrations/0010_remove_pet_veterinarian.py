# Generated by Django 5.0.1 on 2024-01-23 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_rename_owner_pet_veterinarian'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='veterinarian',
        ),
    ]
