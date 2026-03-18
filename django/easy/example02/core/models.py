from django.db import models


class CandidateProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    id_card = models.CharField(max_length=20)  # 明文敏感信息
    phone = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=30)  # 不必要收集
    religion = models.CharField(max_length=50)  # 不必要收集
    medical_history = models.TextField(blank=True)  # 不必要收集
    created_at = models.DateTimeField(auto_now_add=True)
