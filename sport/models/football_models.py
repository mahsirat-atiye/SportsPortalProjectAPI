from django.contrib.auth.models import User
from django.db import models

from sport.models.abstract_models import Human, Event, Player, Game, Team, League

FOOTBALL_PLAYER_EVENT_CHOICES = (
    ('G', 'گل'),
    ('PG', 'پاس گل'),
    ('YC', 'کارت زرد'),
    ('RC', 'کارت قرمز'),
    ('E', 'خطا'),
    ('P', 'پنالتی'),
    ('CH', 'تعویض'),
    ('CO', 'کرنر'),
    ('SG', 'موقعیت گل'),
)

FOOTBALL_POST_CHOICES = (
    ('G', 'دروازه بان'),
    ('HB', 'هاف بک'),
    ('HF', 'هاف فرانت'),
)

FOOTBALL_NON_PLAYER_POST_CHOICES = (
    ('C', 'مربی'),
    ('CH', 'کمک مربی'),
)


class FootballTeam(Team):
    pass


class FootballGame(Game):
    first_team = models.OneToOneField(FootballTeam, on_delete=models.CASCADE)
    second_team = models.OneToOneField(FootballTeam, on_delete=models.CASCADE)


class FootballPlayer(Player):
    team = models.ForeignKey(FootballTeam, on_delete=models.CASCADE)
    post = models.CharField(max_length=2, choices=FOOTBALL_POST_CHOICES)


class FootballEvent(Event):
    game = models.ForeignKey(FootballGame, on_delete=models.CASCADE)  # ?
    event_type = models.CharField(max_length=3, choices=FOOTBALL_PLAYER_EVENT_CHOICES)
    doer = models.ForeignKey(FootballPlayer, on_delete=models.CASCADE)  # ?


class FootballNonPlayer(Human):
    team = models.ForeignKey(FootballTeam, on_delete=models.CASCADE)
    post = models.CharField(max_length=2, choices=FOOTBALL_NON_PLAYER_POST_CHOICES)


class FootballLeague(League):
    pass
