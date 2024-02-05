# Generated by Django 4.2.9 on 2024-01-21 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("published_date", models.DateTimeField(auto_now_add=True)),
                ("slug", models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
