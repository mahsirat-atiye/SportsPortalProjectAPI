from django.urls import path

from sport.views import *
from . import views

app_name = "sport"
urlpatterns = [

    path('recent-news/general/football', recent_general_news, name='last-ten'),
    path('<int:news_id>/news-detail', news_detail_view, name='news-detail'),
    path('teams/football', football_teams, name='football_teams'),
    path('<int:team_id>/football/team-detail', football_team_detail_view, name='football-team-detail'),

]
