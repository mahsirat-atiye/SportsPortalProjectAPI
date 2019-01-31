from django.contrib.auth.models import User
from django.db import models

from sport.models.football_models import TEAM_SITUATION_IN_GAME
from sport.models.abstract_models import Game, Human, Event, Player, Team, League, Image, Video

BASKETBALL_PLAYER_EVENT_CHOICES = (
    ('2PT', 'پرتاب دو امتیازی'),
    ('3PT', 'پرتاب سه امتیازی'),
    ('E', 'خطا'),
    ('R', 'ریباند'),
    ('P', 'پنالتی'),
    ('LP', 'از دست دادن پنالتی'),
    ('CH', 'تعویض'),
)

BASKETBALL_POST_CHOICES = (
    ('G', 'گارد'),
    ('C', 'مرکز'),
    ('GF', 'گارد فوروارد'),
    ('FG', 'فوروارد گارد'),
    ('FC', 'فوروارد سنتر'),
)

BASKETBALL_NON_PLAYER_POST_CHOICES = (
    ('C', 'مربی'),
    ('CH', 'کمک مربی'),
)


class BasketballTeam(Team):
    followers = models.ManyToManyField(User, blank=True, null=True)


class BasketballLeague(League):
    pass


class BasketballGame(Game):
    league = models.ForeignKey(BasketballLeague, on_delete=models.CASCADE, blank=True, null=True)


class BasketballPlayer(Player):
    team = models.ForeignKey(BasketballTeam, on_delete=models.CASCADE)
    post = models.CharField(max_length=2, choices=BASKETBALL_POST_CHOICES)


class BasketballEvent(Event):
    game = models.ForeignKey(BasketballGame, on_delete=models.CASCADE)  # ?
    event_type = models.CharField(max_length=3, choices=BASKETBALL_PLAYER_EVENT_CHOICES)
    doer = models.ForeignKey(BasketballPlayer, on_delete=models.CASCADE)  # ?

    def __str__(self):
        s = self.doer.first_name + " " + self.doer.last_name + " در بازی " + str(
            self.game.date) + "انجام داد" + self.event_type
        return s


class BasketballNonPlayer(Human):
    team = models.ForeignKey(BasketballTeam, on_delete=models.CASCADE)
    post = models.CharField(max_length=2, choices=BASKETBALL_NON_PLAYER_POST_CHOICES)


class BasketballTeamInBasketballGame(models.Model):
    game = models.ForeignKey(BasketballGame, on_delete=models.CASCADE)
    team = models.ForeignKey(BasketballTeam, on_delete=models.CASCADE)

    team_score_Q1 = models.IntegerField(blank=True, null=True)
    team_score_Q2 = models.IntegerField(blank=True, null=True)
    team_score_Q3 = models.IntegerField(blank=True, null=True)
    team_score_Q4 = models.IntegerField(blank=True, null=True)

    property_percent = models.IntegerField(blank=True, null=True)
    situation = models.CharField(max_length=3, choices=TEAM_SITUATION_IN_GAME, blank=True, null=True)
    best_player = models.ForeignKey(BasketballPlayer, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        s = self.team.name + " در بازی " + str(self.game.date)
        return s


class BasketballPlayerInBasketballGame(models.Model):
    game = models.ForeignKey(BasketballGame, on_delete=models.CASCADE)
    player = models.ForeignKey(BasketballPlayer, on_delete=models.CASCADE)
    main_player = models.BooleanField(blank=True, null=True)
    time_of_change = models.TimeField(blank=True, null=True)

    def __str__(self):
        s = self.player.first_name + "  " + self.player.last_name
        " در بازی " + str(self.game.date)
        return s


class BasketballImage(Image):
    game = models.ForeignKey(BasketballGame, on_delete=models.CASCADE, blank=True, null=True)
    team = models.ForeignKey(BasketballTeam, on_delete=models.CASCADE, blank=True, null=True)


class BasketballVideo(Video):
    game = models.ForeignKey(BasketballGame, on_delete=models.CASCADE, blank=True, null=True)
