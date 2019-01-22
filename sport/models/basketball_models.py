from django.contrib.auth.models import User
from django.db import models

from sport.models.abstract_models import Game, Human, Event, Player, Team

BASKETBALL_PLAYER_EVENT_CHOICES = (
    ('2PT', 'پرتاب دو امتیازی'),
    ('3PT', 'پرتاب سه امتیازی'),
    ('E', 'خطا'),
    ('R', 'ریباند'),
)

BASKETBALL_POST_CHOICES = (
    ('RB', 'بسکتبالیست چپ'),
    ('LB', 'بسکتبالیست راست'),
    ('MB', 'بسکتبالیست اصلی'),
)

BASKETBALL_NON_PLAYER_POST_CHOICES = (
    ('C', 'مربی'),
    ('CH', 'کمک مربی'),
)


class BasketballTeam(Team):
    pass


class BasketballGame(Game):
    first_team = models.OneToOneField(BasketballTeam, on_delete=models.CASCADE)
    second_team = models.OneToOneField(BasketballTeam, on_delete=models.CASCADE)


class BasketballPlayer(Player):
    team = models.ForeignKey(BasketballTeam, on_delete=models.CASCADE)
    post = models.CharField(max_length=2, choices=BASKETBALL_POST_CHOICES)


class BasketballEvent(Event):
    game = models.ForeignKey(BasketballGame, on_delete=models.CASCADE)  # ?
    event_type = models.CharField(max_length=3, choices=BASKETBALL_PLAYER_EVENT_CHOICES)
    doer = models.ForeignKey(BasketballPlayer, on_delete=models.CASCADE)  # ?


class BasketballNonPlayer(Human):
    team = models.ForeignKey(BasketballTeam, on_delete=models.CASCADE)
    post = models.CharField(max_length=2, choices=BASKETBALL_NON_PLAYER_POST_CHOICES)
