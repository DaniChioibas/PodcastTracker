# Generated by Django 4.2.7 on 2023-11-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("podcasts", "0003_podcast_vote_ratio_podcast_vote_total"),
    ]

    operations = [
        migrations.AddField(
            model_name="podcast",
            name="featured_image",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to=""
            ),
        ),
    ]
