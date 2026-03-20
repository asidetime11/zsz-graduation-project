from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    id_card = models.CharField(max_length=64)
    phone = models.CharField(max_length=32)
    consent_flag = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id}-{self.org_id}"


class BehaviorProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tracking_id = models.CharField(max_length=120)
    behavior_data = models.JSONField(default=dict)
    third_party_synced = models.BooleanField(default=False)
    synced_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.tracking_id


class ThirdPartySync(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    api_endpoint = models.CharField(max_length=255)
    payload_snapshot = models.JSONField(default=dict)
    triggered_by = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id}-{self.api_endpoint}"


class BehaviorLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payload = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)
