from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=32, blank=True)
    id_card = models.CharField(max_length=64)
    ssn = models.CharField(max_length=64)
    bank_account = models.CharField(max_length=64)
    password_hash = models.CharField(max_length=255)
    failed_login_count = models.IntegerField(default=0)
    last_login = models.DateTimeField(null=True, blank=True)
    internal_flags = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.username


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, related_name="following_edges", on_delete=models.CASCADE)
    following = models.ForeignKey(UserProfile, related_name="follower_edges", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower_id}->{self.following_id}"
