from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    feedback_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
