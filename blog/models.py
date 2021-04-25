from django.db import models

class Post(models.Model):
  title=models.CharField(max_length=150)
  desc=models.TextField()
  author=models.CharField(max_length=150)
  created_date=models.DateTimeField(auto_now_add=True)
  updated_date=models.DateTimeField(auto_now=True)

