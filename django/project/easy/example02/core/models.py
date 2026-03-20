from django.db import models


class CandidateProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    id_card = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=30)
    religion = models.CharField(max_length=50)
    medical_history = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
