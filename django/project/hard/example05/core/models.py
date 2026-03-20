from django.contrib.auth.models import User
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Department(models.Model):
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.org.name}-{self.name}"


class Document(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file_path = models.CharField(max_length=255)
    owner_id_card = models.CharField(max_length=64)
    internal_notes = models.TextField(blank=True)
    salary_info = models.CharField(max_length=128, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AccessLog(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True)
    user_credential_hint = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.document.pk}-{self.user.pk}-{self.action}"
