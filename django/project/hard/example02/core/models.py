from django.db import models


class UserAccount(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    ssn = models.CharField(max_length=64)
    bank_account = models.CharField(max_length=64)
    card_number = models.CharField(max_length=32)
    cvv = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.username}-{self.bank_account}"


class APIIntegration(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=200)
    api_secret = models.CharField(max_length=200)
    webhook_secret = models.CharField(max_length=200)
    private_key = models.TextField()

    def __str__(self):
        return f"{self.user.username}-{self.service_name}"


class Transaction(models.Model):
    from_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="outgoing_transactions")
    to_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="incoming_transactions")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    card_number = models.CharField(max_length=32)
    status = models.CharField(max_length=32, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}:{self.from_account_id}->{self.to_account_id}"
