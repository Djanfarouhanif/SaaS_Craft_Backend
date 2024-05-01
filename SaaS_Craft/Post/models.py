from django.db import models
import uuid
from datetime import datetime
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Article(models.Model):
    id = models.CharField(max_length=500, default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=100)
    post = models.TextField()
    post_image = models.ImageField(upload_to="post_image")
    date_to_create = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
    date_to_create = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.article.title


