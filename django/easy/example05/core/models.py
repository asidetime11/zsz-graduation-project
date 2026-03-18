from django.db import models


class ParcelRecord(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    id_card = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    parcel_no = models.CharField(max_length=50)
    status = models.CharField(max_length=30, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
