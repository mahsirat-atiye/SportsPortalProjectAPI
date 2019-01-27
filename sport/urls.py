from django.urls import path, include

from sport.views import *
from . import views

app_name = "sport"
urlpatterns = [

    path('home/general/', recent_general_news, name='general-home'),
    path('<int:news_id>/news-detail', news_detail_view, name='news-detail'),
    path('', football_teams, name='football_teams'),
    path('<int:team_id>/football/team-detail', football_team_detail_view, name='football-team-detail'),
    path('<int:player_id>/football/player-detail', football_player_detail_view, name='football-player-detail'),
    path('<int:game_id>/football/game-detail', football_game_detail_view, name='football-game-detail'),
    path('leagues/football', football_leagues, name='football_leagues'),
    path('<int:league_id>/league_detail', league_detail, name='league_detail'),

    path('accounts/', include('django.contrib.auth.urls')),  # new
    path('accounts/signup/', signup, name='signup'),
    path('accounts/login/', login, name='login'),
]
