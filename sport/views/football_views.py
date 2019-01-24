from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from sport.models import News, FootballTeam, FootballPlayer, FootballGame
from django.utils import timezone


#
# class RecentGeneralNews(generic.ListView):
#     template_name = 'sport/recent_general_news.html'
#     context_object_name = 'recent_news'
#
#     def get_queryset(self):
#         return News.objects.filter(publish_date__lte=timezone.now()).filter(type='F').order_by('-publish_date')[:10]


def recent_general_news(request):
    if request.POST:
        n = int(request.POST['number'])
        recent_news = News.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')[:n]
    else:
        recent_news = News.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')[:10]

    context = {
        'recent_news': recent_news
    }
    return render(request, 'sport/recent_general_news.html', context)


def football_teams(request):
    teams = FootballTeam.objects.all()

    context = {
        'teams': teams
    }
    return render(request, 'sport/teams.html', context)


def football_team_detail_view(request, team_id):
    related_news = set([])
    news = News.objects.all()
    team = get_object_or_404(FootballTeam, pk=team_id)

    if request.POST:
        if request.POST["part"] == 'filter_games':

            if request.POST['choice'] == 'opponent_team':
                team_in_games = team.footballteaminfootballgame_set.all()

                games = []
                for tg in team_in_games:
                    games.append(tg.game)

                def sort_by_opponent(g):
                    teams_in_game = g.footballteaminfootballgame_set.all()
                    if teams_in_game[0].team == team:
                        return teams_in_game[1].team.name
                    return teams_in_game[0].team.name

                games.sort(key=sort_by_opponent)
            else:
                team_in_games = team.footballteaminfootballgame_set.all().order_by('team_score')
                games = []
                for tg in team_in_games:
                    games.append(tg.game)
            for n in news:
                for t in n.tag_set.all():
                    if t.text.__contains__(team.name):
                        related_news.add(n)
                if n.title.__contains__(team.name):
                    related_news.add(n)
                if n.text.__contains__(team.name):
                    related_news.add(n)
        else:
            if request.POST["choice"] == 'tag':
                for n in news:
                    for t in n.tag_set.all():
                        if t.text.__contains__(team.name):
                            related_news.add(n)

            elif request.POST["choice"] == 'title':
                for n in news:

                    if n.title.__contains__(team.name):
                        related_news.add(n)

            else:
                for n in news:

                    if n.text.__contains__(team.name):
                        related_news.add(n)
            games = []
            team_in_games = team.footballteaminfootballgame_set.all()
            for tg in team_in_games:
                games.append(tg.game)

            def sort_game_by_date(g):
                return g.date

            games.sort(key=sort_game_by_date, reverse=True)
    else:
        team_in_games = team.footballteaminfootballgame_set.all()
        games = []
        for tg in team_in_games:
            games.append(tg.game)

        def sort_game_by_date(g):
            return g.date

        games.sort(key=sort_game_by_date, reverse=True)

        for n in news:
            for t in n.tag_set.all():
                if t.text.__contains__(team.name):
                    related_news.add(n)
            if n.title.__contains__(team.name):
                related_news.add(n)
            if n.text.__contains__(team.name):
                related_news.add(n)
    related_news = list(related_news)

    context = {
        'team': team,
        'related_news': related_news,
        'games': games
    }

    return render(request, 'sport/football_team_detail.html', context)


def football_player_detail_view(request, player_id):
    player = get_object_or_404(FootballPlayer, pk=player_id)
    context = {
        'player': player
    }
    return render(request, 'sport/football_player_detail.html', context)


def football_game_detail_view(request, game_id):
    game = get_object_or_404(FootballGame, pk=game_id)
    context = {
        'game': game
    }
    return render(request, 'sport/football_player_detail.html', context)
