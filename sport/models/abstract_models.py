from django.contrib.auth.models import User
from django.db import models

from sport.models.general_models import News


class Human(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_day = models.DateField()
    height = models.IntegerField()
    weight = models.IntegerField()
    image = models.ImageField(upload_to='human_images', blank=True)

    def __str__(self):
        s = self.first_name + " " + self.last_name
        return s

    class Meta:
        abstract = True


class League(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        s = self.name + " " + str(self.year) + " - " + str(self.year+1)
        return s


class Team(models.Model):
    name = models.CharField(max_length=100)


    # news = models.ManyToManyField(News)
    def __str__(self):
        s = self.name
        return s

    class Meta:
        abstract = True


#     players & non players handled by one-to-one


class Game(models.Model):
    report = models.TextField(blank=True, null=True)

    date = models.DateField()

    def __str__(self):
        s = str(self.date)
        return s

    # league = models.ForeignKey(League, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date',)
        abstract = True


#     get recent games in 3 days!
#       order by win, loose, equal  OR  order by other team ==> filter by js


class Event(models.Model):
    exact_time = models.DateTimeField()

    class Meta:
        ordering = ('-exact_time',)
        abstract = True


class Player(Human):
    # team = models.ForeignKey(Team, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User)
    news = models.ManyToManyField(News)

    # order by post js
    class Meta:
        abstract = True


class Image(models.Model):
    caption = models.CharField(max_length=250, default="")
    image = models.ImageField(upload_to='general_images', blank=True)
    # football_game = models.ForeignKey(FootballGame, on_delete=models.CASCADE, blank=True, null=True)
    news = models.ManyToManyField(News, blank=True, null=True)

    def __str__(self):
        s = self.caption
        return s

    class Meta:
        abstract = True


class Video(models.Model):
    caption = models.CharField(max_length=250, default="")
    video = models.FileField(upload_to='general_videos', blank=True, null=True)

    def __str__(self):
        s = self.caption
        return s

    class Meta:
        abstract = True
