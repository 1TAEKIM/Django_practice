# Generated by Django 5.0.4 on 2024-04-12 01:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0002_movie_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
    ]
