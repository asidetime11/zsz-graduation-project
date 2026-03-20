from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=120)
    id_card = models.CharField(max_length=64)
    phone = models.CharField(max_length=32)
    card_number = models.CharField(max_length=32)
    cvv = models.CharField(max_length=8)

    def __str__(self):
        return self.name


class ExportTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=32, default="pending")
    file_path = models.CharField(max_length=255, blank=True)
    task_payload = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}-{self.user.username}-{self.status}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.sent_at}"
