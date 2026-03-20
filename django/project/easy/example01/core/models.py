from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    id_card = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    bank_account = models.CharField(max_length=50)
    family_members = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.phone})"
