from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)  # 明文敏感数据

    def __str__(self):
        return self.username


class PaymentInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    card_number = models.CharField(max_length=32)  # 明文敏感数据
    cvv = models.CharField(max_length=4)  # 明文敏感数据
    expiry_date = models.CharField(max_length=8)  # 明文敏感数据
    api_token = models.CharField(max_length=200)  # 明文敏感数据
    bank_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}-{self.bank_name}"
