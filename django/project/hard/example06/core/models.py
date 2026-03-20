from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    id_card = models.CharField(max_length=64)
    ssn = models.CharField(max_length=64)
    phone = models.CharField(max_length=32)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    bank_account = models.CharField(max_length=64)
    medical_info = models.TextField(blank=True)
    home_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PayrollTask(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    card_number = models.CharField(max_length=64)
    status = models.CharField(max_length=32, default="pending")
    task_log = models.TextField(blank=True)

    def __str__(self):
        return f"{self.employee.name}-{self.amount}-{self.status}"
