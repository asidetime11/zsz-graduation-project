from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Organization",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("api_key", models.CharField(max_length=200)),
                ("webhook_secret", models.CharField(max_length=200)),
                (
                    "owner",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PaymentCard",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("card_number", models.CharField(max_length=16)),
                ("cvv", models.CharField(max_length=4)),
                ("expiry_date", models.CharField(max_length=5)),
                (
                    "organization",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="core.organization"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Report",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("data", models.JSONField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "created_by",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="created_reports", to=settings.AUTH_USER_MODEL),
                ),
                (
                    "organization",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="reports", to="core.organization"),
                ),
            ],
        ),
    ]
