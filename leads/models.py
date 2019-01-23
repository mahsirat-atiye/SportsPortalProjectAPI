from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
