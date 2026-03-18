from django.db import models


class UserProfile(models.Model):
    """用户注册信息（含敏感信息）。"""

    name = models.CharField(max_length=100)
    id_card = models.CharField(max_length=20)  # 明文存储敏感信息
    phone = models.CharField(max_length=20)  # 明文存储敏感信息
    bank_account = models.CharField(max_length=50)  # 明文存储敏感信息
    family_members = models.IntegerField(default=0)  # 与注册目标弱相关，存在数据最小化问题
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.phone})"
