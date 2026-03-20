from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    id_card = models.CharField(max_length=32)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.username


class Survey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SurveyResponse(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="responses")
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="responses")
    answers = models.TextField()
    family_income = models.CharField(max_length=128)
    submitted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f"{self.user.username}-{self.survey.title}"
