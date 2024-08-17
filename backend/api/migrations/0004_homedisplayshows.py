# Generated by Django 4.2.15 on 2024-08-14 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_carouselimage_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomeDisplayShows",
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
                ("title", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="HomepageEvent_images/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
