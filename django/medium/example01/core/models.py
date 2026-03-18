from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)  # 明文敏感数据
    id_card = models.CharField(max_length=30)  # 明文敏感数据
    passport_no = models.CharField(max_length=30)  # 明文敏感数据

    def __str__(self):
        return self.username


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    items = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    payment_card = models.CharField(max_length=30)  # 明文敏感数据
    status = models.CharField(max_length=30, default="pending")
    passport_no = models.CharField(max_length=30, blank=True, default="")  # 与购物无关，数据最小化问题

    def __str__(self):
        return f"Order#{self.id} - {self.user.username}"
