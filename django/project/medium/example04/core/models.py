from django.db import models


class UserProfile(models.Model):
	username = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	id_card = models.CharField(max_length=32)
	occupation = models.CharField(max_length=120)
	medical_history = models.TextField()
	marketing_agree = models.BooleanField(default=True)

	def __str__(self):
		return self.username


class Article(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="articles")
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
	author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="comments")
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
