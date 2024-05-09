# Generated by Django 5.0.5 on 2024-05-07 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="address",
            name="person",
        ),
        migrations.AddField(
            model_name="address",
            name="persons",
            field=models.ManyToManyField(to="myapp.person"),
        ),
    ]
