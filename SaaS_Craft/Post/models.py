from django.db import models
import uuid
from datetime import datetime
# Create your models here.


class Article(models.Model):
    id = models.CharField(max_length=500, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    post = models.TextField()
    post_image = models.ImageField(upload_to="post_image")
    date_to_cteate = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeingKey(Article, on_delete=models.CASCADE)
    text = models.textField()
    date_to_create = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.date_to_create


