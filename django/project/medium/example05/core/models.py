from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    bank_account = models.CharField(max_length=64)

    def __str__(self):
        return self.username


class Transaction(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    card_number = models.CharField(max_length=32)
    status = models.CharField(max_length=30, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.amount}-{self.status}"
