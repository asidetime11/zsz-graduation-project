from django.db import models


class StudentProfile(models.Model):
    name = models.CharField(max_length=100)
    id_card = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    gpa = models.FloatField(default=0)
    family_income = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
