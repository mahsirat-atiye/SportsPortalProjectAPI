from django.contrib.auth.models import User
from django.db import models


TYPE_CHOICES = (
    ('F', 'فوتبال'),
    ('B', 'بسکتبال')
)


class News(models.Model):
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='F')
    title = models.CharField(max_length=100)
    text = models.TextField()
    publish_date = models.DateField()

    def __str__(self):
        s = self.title
        return s


# tags and resources and related teams and related players were handled by many to many relationship

#     todo : images of non News

# recent news needed! during last 10/2 days


class Resource(models.Model):
    name = models.CharField(max_length=100)
    news = models.ManyToManyField(News)


#     many resources for many pieces of news!


class Tag(models.Model):
    text = models.CharField(max_length=100)
    news = models.ManyToManyField(News)

    def __str__(self):
        s = self.text
        return s


#     many tags for many pieces of news!


class Comment(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)






# class FootballPlayerInGame(models.Model):
#     game = models.ForeignKey(Game, on_delete=models.CASCADE)
#     player = models.ForeignKey(Player,)
#
