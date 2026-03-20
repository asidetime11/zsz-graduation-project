from django.db import models


class UserAccount(models.Model):
    username = models.CharField(max_length=120)
    password_hash = models.CharField(max_length=255)
    email = models.EmailField()
    card_number = models.CharField(max_length=64)
    api_key = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Transaction(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    card_number = models.CharField(max_length=64)
    status = models.CharField(max_length=32)
    audit_trail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.amount}-{self.status}"


class AuditLog(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    sql_snippet = models.TextField()
    card_number = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.action}"


class BackupRecord(models.Model):
    file_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_path
