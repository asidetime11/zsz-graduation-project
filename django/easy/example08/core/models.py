from django.db import models


class SupportTicket(models.Model):
    name = models.CharField(max_length=100)
    id_card = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    ticket_content = models.TextField()
    status = models.CharField(max_length=30, default="open")
    created_at = models.DateTimeField(auto_now_add=True)
