from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateField()
    location = models.CharField(max_length=200)
    max_participants = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Participant(models.Model):
    user_name = models.CharField(max_length=100)
    id_card = models.CharField(max_length=32)
    phone = models.CharField(max_length=20)
    passport_no = models.CharField(max_length=32)
    medical_history = models.TextField()
    marital_status = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    family_income = models.CharField(max_length=120)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="participants")
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
