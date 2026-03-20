
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PatientProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("id_card", models.CharField(max_length=32)),
                ("phone", models.CharField(max_length=20)),
                ("medical_history", models.TextField()),
                ("allergies", models.TextField(blank=True)),
                ("emergency_contact_id", models.CharField(max_length=64)),
                ("marketing_agree", models.BooleanField(default=True)),
                ("data_collection_consent", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Appointment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("doctor_name", models.CharField(max_length=100)),
                ("date", models.DateField()),
                ("reason", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "patient",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="appointments", to="core.patientprofile"),
                ),
            ],
        ),
    ]
