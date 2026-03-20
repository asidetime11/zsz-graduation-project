
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Survey",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("username", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                ("id_card", models.CharField(max_length=32)),
                ("ip_address", models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name="SurveyResponse",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("answers", models.TextField()),
                ("family_income", models.CharField(max_length=128)),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                ("ip_address", models.GenericIPAddressField()),
                (
                    "survey",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="responses", to="core.survey"),
                ),
                (
                    "user",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="responses", to="core.userprofile"),
                ),
            ],
        ),
    ]
