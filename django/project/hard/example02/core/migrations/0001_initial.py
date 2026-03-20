
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserAccount",
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
                ("username", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=32)),
                ("ssn", models.CharField(max_length=64)),
                ("bank_account", models.CharField(max_length=64)),
                ("card_number", models.CharField(max_length=32)),
                ("cvv", models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
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
                ("amount", models.DecimalField(decimal_places=2, max_digits=12)),
                ("card_number", models.CharField(max_length=32)),
                ("status", models.CharField(default="pending", max_length=32)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "from_account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="outgoing_transactions",
                        to="core.useraccount",
                    ),
                ),
                (
                    "to_account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="incoming_transactions",
                        to="core.useraccount",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="APIIntegration",
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
                ("service_name", models.CharField(max_length=100)),
                ("api_key", models.CharField(max_length=200)),
                ("api_secret", models.CharField(max_length=200)),
                ("webhook_secret", models.CharField(max_length=200)),
                ("private_key", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.useraccount",
                    ),
                ),
            ],
        ),
    ]
