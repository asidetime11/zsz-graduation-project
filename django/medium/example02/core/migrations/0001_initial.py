from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("username", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="PaymentInfo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("card_number", models.CharField(max_length=32)),
                ("cvv", models.CharField(max_length=4)),
                ("expiry_date", models.CharField(max_length=8)),
                ("api_token", models.CharField(max_length=200)),
                ("bank_name", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="payments", to="core.user"),
                ),
            ],
        ),
    ]
