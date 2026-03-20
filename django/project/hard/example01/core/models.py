from django.contrib.auth.models import User
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=200)
    webhook_secret = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Report(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    data = models.JSONField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.organization.name}-{self.title}"


class PaymentCard(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=4)
    expiry_date = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.organization.name}-{self.card_number[-4:]}"
