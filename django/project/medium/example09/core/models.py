from django.db import models


class UserAccount(models.Model):
    username = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    id_card = models.CharField(max_length=32)
    api_token = models.CharField(max_length=64, default="")
    internal_status = models.CharField(max_length=32, default="active")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class LoginAudit(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, related_name="login_logs")
    request_body = models.TextField(default="")
    ip_address = models.CharField(max_length=64, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id}-{self.created_at}"
