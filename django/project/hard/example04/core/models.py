from django.contrib.auth.models import User
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    id_card = models.CharField(max_length=64)
    ssn = models.CharField(max_length=64)
    bank_account = models.CharField(max_length=64)
    phone = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.user.username}-{self.org.name}"


class CacheRecord(models.Model):
    cache_key = models.CharField(max_length=255)
    cached_data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cache_key
