from django.urls import path, include

from sport.views import *
from . import views

app_name = "sport"
urlpatterns = [
    # general

    path('', recent_general_news_games, name='home'),
    path('<int:news_id>/news-detail', news_detail_view, name='news-detail'),
    path('accounts/', include('django.contrib.auth.urls')),  # new
    path('accounts/signup/', signup, name='signup'),
    path('accounts/login/', login, name='login'),

    # football

    path('football/teams', football_teams, name='football_teams'),
    path('<int:team_id>/football/team-detail', football_team_detail_view, name='football-team-detail'),
    path('<int:player_id>/football/player-detail', football_player_detail_view, name='football-player-detail'),
    path('<int:game_id>/football/game-detail', football_game_detail_view, name='football-game-detail'),
    path('football/leagues', football_leagues, name='football_leagues'),
    path('<int:league_id>/football/league_detail', football_league_detail, name='league_detail_football'),

    # basketball

    path('basketball/teams', basketball_teams, name='basketball_teams'),
    path('<int:team_id>/basketball/team-detail', basketball_team_detail_view, name='basketball-team-detail'),
    path('<int:player_id>/basketball/player-detail', basketball_player_detail_view, name='basketball-player-detail'),
    path('<int:game_id>/basketball/game-detail', basketball_game_detail_view, name='basketball-game-detail'),
    path('basketball/leagues', basketball_leagues, name='football_leagues'),
    path('<int:league_id>/basketball/league_detail', basketball_league_detail, name='league_detail_basketball'),

]
