from django.db import models


class UserProfile(models.Model):
	username = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	bio = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.username


class Post(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="posts")
	title = models.CharField(max_length=200)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
