from django.db import models


class VisitorLog(models.Model):
    name = models.CharField(max_length=100)
    id_card = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=200)
    visit_reason = models.CharField(max_length=200)
    host_name = models.CharField(max_length=100)
    visit_time = models.DateTimeField()
