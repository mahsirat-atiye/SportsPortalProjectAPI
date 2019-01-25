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

TEAM_SITUATION_IN_GAME = (
    ('AW', 'برد'),
    ('BE', 'مساوی'),
    ('CL', 'باخت')
)
class FootballTeam(Team):
    pass


class FootballGame(Game):
    # teams = models.ManyToManyField(FootballTeam)
    pass


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


class FootballTeamInFootballGame(models.Model):
    game = models.ForeignKey(FootballGame, on_delete=models.CASCADE)
    team = models.ForeignKey(FootballTeam, on_delete=models.CASCADE)
    team_score = models.IntegerField(blank=True, null=True)
    property_percent = models.IntegerField(blank=True, null=True)
    situation = models.CharField(max_length=3, choices=TEAM_SITUATION_IN_GAME, blank=True, null=True)


class FootballPlayerInFootballGame(models.Model):
    game = models.ForeignKey(FootballGame, on_delete=models.CASCADE)
    player = models.ForeignKey(FootballPlayer, on_delete=models.CASCADE)
    main_player = models.BooleanField(blank=True, null=True)
    time_of_change = models.TimeField(blank=True, null=True)
