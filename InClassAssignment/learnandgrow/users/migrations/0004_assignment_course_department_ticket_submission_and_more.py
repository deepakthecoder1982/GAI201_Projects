# Generated by Django 4.2.4 on 2023-09-08 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_customuser_role"),
    ]

    operations = [
        migrations.CreateModel(
            name="Assignment",
            fields=[
                ("assign_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=50)),
                ("Description", models.TextField()),
                ("Due_Date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                ("course_id", models.AutoField(primary_key=True, serialize=False)),
                ("course_name", models.CharField(max_length=100)),
                ("credits", models.PositiveIntegerField()),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                ("de_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                ("resolve_date", models.DateTimeField(auto_created=True)),
                ("create_date", models.DateTimeField(auto_created=True)),
                ("ticket_id", models.AutoField(primary_key=True, serialize=False)),
                ("topic", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("resolved", "Resolved"),
                            ("not-resolved", "not-resolved"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "course_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.course"
                    ),
                ),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.student"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Submission",
            fields=[
                ("submis_id", models.AutoField(primary_key=True, serialize=False)),
                ("Submission_date", models.DateTimeField(auto_now_add=True)),
                (
                    "Assignment_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.assignment",
                    ),
                ),
                (
                    "course_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.course"
                    ),
                ),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.student"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Enrollment",
            fields=[
                ("Enrollment_id", models.AutoField(primary_key=True, serialize=False)),
                ("Enrollment_date", models.DateTimeField(auto_now_add=True)),
                (
                    "course_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.course"
                    ),
                ),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.student"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.department"
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="instructor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.instructor"
            ),
        ),
        migrations.AddField(
            model_name="assignment",
            name="Course_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.course"
            ),
        ),
    ]