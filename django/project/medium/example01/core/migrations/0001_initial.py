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
                ("id_card", models.CharField(max_length=30)),
                ("passport_no", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("items", models.TextField()),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("address", models.CharField(max_length=255)),
                ("payment_card", models.CharField(max_length=30)),
                ("status", models.CharField(default="pending", max_length=30)),
                ("passport_no", models.CharField(blank=True, default="", max_length=30)),
                (
                    "user",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="orders", to="core.user"),
                ),
            ],
        ),
    ]
