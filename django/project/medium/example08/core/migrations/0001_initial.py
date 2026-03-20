
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Activity",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("date", models.DateField()),
                ("location", models.CharField(max_length=200)),
                ("max_participants", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Participant",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("user_name", models.CharField(max_length=100)),
                ("id_card", models.CharField(max_length=32)),
                ("phone", models.CharField(max_length=20)),
                ("passport_no", models.CharField(max_length=32)),
                ("medical_history", models.TextField()),
                ("marital_status", models.CharField(max_length=50)),
                ("religion", models.CharField(max_length=50)),
                ("family_income", models.CharField(max_length=120)),
                ("registered_at", models.DateTimeField(auto_now_add=True)),
                (
                    "activity",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="participants", to="core.activity"),
                ),
            ],
        ),
    ]
