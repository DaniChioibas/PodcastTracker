# Generated by Django 4.2.7 on 2023-12-02 11:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0002_profile_username"),
    ]

    operations = [
        migrations.CreateModel(
            name="Podcast",
            fields=[
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "featured_image",
                    models.ImageField(
                        blank=True, default="default.jpg", null=True, upload_to=""
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("vote_total", models.IntegerField(blank=True, default=0, null=True)),
                ("vote_ratio", models.FloatField(blank=True, default=0, null=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
            options={
                "ordering": ["-vote_total", "-vote_ratio"],
            },
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "value",
                    models.IntegerField(
                        choices=[
                            (1, "1 Star"),
                            (2, "2 Stars"),
                            (3, "3 Stars"),
                            (4, "4 Stars"),
                            (5, "5 Stars"),
                        ]
                    ),
                ),
                ("body", models.TextField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.profile",
                    ),
                ),
                (
                    "podcast",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="podcasts.podcast",
                    ),
                ),
            ],
            options={
                "unique_together": {("owner", "podcast")},
            },
        ),
    ]
