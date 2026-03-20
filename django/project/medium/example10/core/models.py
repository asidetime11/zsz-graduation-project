from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    id_card = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class UserActivity(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name="activities")
    action = models.CharField(max_length=120)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.action}-{self.timestamp}"
