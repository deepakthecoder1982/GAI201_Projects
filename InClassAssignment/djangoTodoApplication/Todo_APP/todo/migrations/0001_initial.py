# Generated by Django 4.2.4 on 2023-09-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TodoModel",
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
                ("title", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=100)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("InProgress", "InProgress"),
                            ("Completed", "Completed"),
                            ("NotStarted", "NotStarted"),
                        ],
                        default="NotStarted",
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]