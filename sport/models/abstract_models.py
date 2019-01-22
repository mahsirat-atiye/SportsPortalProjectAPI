from django.contrib.auth.models import User
from django.db import models

from sport.models.general_models import News


class Human(models.Model):
    sport_type = models.CharField(max_length=1, choices=SPORT_TYPE_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_day = models.DateField()
    height = models.DecimalField(max_digits=2, max_length=5)
    weight = models.DecimalField(max_digits=2, max_length=5)

    #     todo : images of human

    class Meta:
        abstract = True


class League(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()

    class Meta:
        abstract = True


class Team(models.Model):
    name = models.CharField(max_length=100)
    followers = models.ManyToManyField(User)
    news = models.ManyToManyField(News)


#     players & non players handled by one-to-one


class Game(models.Model):
    # first_team = models.OneToOneField(Team, on_delete=models.CASCADE)
    # second_team = models.OneToOneField(Team, on_delete=models.CASCADE)

    first_team_score = models.IntegerField()
    second_team_score = models.IntegerField()

    first_team_percentage_possession = models.IntegerField()
    # must be less than 100

    report = models.TextField(blank=True, null=True)

    date = models.DateField()

    # league = models.ForeignKey(League, on_delete=models.CASCADE)

    class Meta:
        ordering = ('date',)
        abstract = True


#     get recent games in 3 days!
#       order by win, loose, equal  OR  order by other team ==> filter by js


class Event(models.Model):
    exact_time = models.DateTimeField()

    class Meta:
        abstract = True


class Player(Human):
    # team = models.ForeignKey(Team, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User)
    news = models.ManyToManyField(News)

    # order by post js
    class Meta:
        abstract = True



