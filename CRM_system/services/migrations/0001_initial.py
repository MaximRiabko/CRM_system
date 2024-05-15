# Generated by Django 5.0.3 on 2024-05-15 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=8),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contract",
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
                ("name_contract", models.CharField(max_length=255)),
                ("file", models.FileField(upload_to="uploads_document")),
                ("date_conclusion", models.DateTimeField(auto_now_add=True)),
                ("expiration_date", models.DateTimeField(auto_now_add=True)),
                (
                    "summ",
                    models.DecimalField(decimal_places=2, default=0, max_digits=8),
                ),
                (
                    "service_provided",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="services.service",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AdvertisingСompany",
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
                ("company_name", models.CharField(max_length=255)),
                ("promotion_channel", models.CharField(max_length=255)),
                (
                    "budget",
                    models.DecimalField(decimal_places=2, default=0, max_digits=8),
                ),
                (
                    "advertised_service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="services.service",
                    ),
                ),
            ],
        ),
    ]
