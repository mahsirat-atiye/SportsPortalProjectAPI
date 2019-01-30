from django.shortcuts import get_object_or_404, render
from django.views import generic
import datetime

from sport.models import News, FootballGame, BasketballGame, Comment
from django.utils import timezone


class NewsDetailView(generic.DetailView):
    template_name = 'sport/general/news_detail.html'
    context_object_name = 'news'
    model = News


def news_detail_view(request, news_id):
    news = get_object_or_404(News, pk=news_id)

    if request.POST:
        title = request.POST['title']
        text = request.POST['comment']
        writer = request.user
        new_comment = Comment(title=title, text=text, writer=writer, news=news)
        new_comment.save()

    related_news = []
    related_tags = news.tag_set.all()
    for t in related_tags:
        for n in t.news.all():
            related_news.append(n)
    if related_news.__contains__(news):
        related_news.remove(news)
    comments = news.comment_set.all()

    return render(request, 'sport/general/news_detail.html', {
        'news': news,
        'related_news': related_news,
        "comments": comments

    }
                  )


def recent_general_news_games(request):
    football_news = News.objects.filter(type__exact='F').filter(publish_date__lte=timezone.now()).filter(
        publish_date__gte=timezone.now() - datetime.timedelta(days=2)).order_by('-publish_date')

    basketball_news = News.objects.filter(type__exact='B').filter(publish_date__lte=timezone.now()).filter(
        publish_date__gte=timezone.now() - datetime.timedelta(days=2)).order_by('-publish_date')

    football_teams = request.user.footballteam_set.all()  # for debug
    basketball_teams = request.user.basketballplayer_set.all()

    f1_ = request.user.footballteam_set.all()
    f2_ = request.user.footballplayer_set.all()
    f3_ = request.user.basketballteam_set.all()
    f4_ = request.user.basketballplayer_set.all()
    f1 = map(lambda x: x.name, f1_)
    f2 = map(lambda x: str(x), f2_)
    f3 = map(lambda x: str(x), f3_)
    f4 = map(lambda x: str(x), f4_)
    favorites = []
    favorites.extend(f1)
    favorites.extend(f2)
    favorites.extend(f3)
    favorites.extend(f4)

    # games:
    future_football_games = FootballGame.objects.filter(date__gt=timezone.now()).order_by('-date')[:10]
    future_basketball_games = BasketballGame.objects.filter(date__gt=timezone.now()).order_by('-date')[:10]

    football_games = FootballGame.objects.filter(date__lte=timezone.now()).order_by('-date')[:10]
    basketball_games = BasketballGame.objects.filter(date__lte=timezone.now()).order_by('-date')[:10]

    favorite_football_games = FootballGame.objects.filter(
        date__gt=timezone.now() - datetime.timedelta(days=1)).filter(
        date__lte=timezone.now() + datetime.timedelta(days=1)).order_by('-date')[:10]

    favorite_basketball_games = BasketballGame.objects.filter(
        date__gt=timezone.now() - datetime.timedelta(days=1)).filter(
        date__lte=timezone.now() + datetime.timedelta(days=1)).order_by('-date')[:10]

    # news
    favorite_football_news = get_related_news_by_all_criteria(football_news, *favorites)
    favorite_basketball_news = get_related_news_by_all_criteria(basketball_news, *favorites)
    if request.POST:
        n = int(request.POST['number'])
        recent_football_news = News.objects.filter(type__exact='F').filter(publish_date__lte=timezone.now()).order_by(
            '-publish_date')[:n]
        recent_basketball_news = News.objects.filter(type__exact='B').filter(publish_date__lte=timezone.now()).order_by(
            '-publish_date')[:n]

    else:
        recent_football_news = News.objects.filter(type__exact='F').filter(publish_date__lte=timezone.now()).order_by(
            '-publish_date')[:10]
        recent_basketball_news = News.objects.filter(type__exact='B').filter(publish_date__lte=timezone.now()).order_by(
            '-publish_date')[:10]

    context = {
        'recent_football_news ': recent_football_news,
        'recent_basketball_news': recent_basketball_news,

        'favorite_football_news': favorite_football_news,
        'favorite_basketball_news': favorite_basketball_news,

        'football_teams': football_teams,
        'basketball_teams': basketball_teams,

        'future_football_games': future_football_games,
        'future_basketball_games': future_basketball_games,

        'football_games': football_games,
        'basketball_games': basketball_games,

        'favorite_football_games': favorite_football_games,
        'favorite_basketball_games': favorite_basketball_games

    }
    return render(request, 'sport/general/general_home_page.html', context)


#  ---------------------------------------------------------------------------------------




def get_related_news_by_all_criteria(news, *special_text):
    related_news = set([])
    for st in special_text:
        for n in news:
            for t in n.tag_set.all():
                if t.text.__contains__(st):
                    related_news.add(n)
            if n.title.__contains__(st):
                related_news.add(n)
            if n.text.__contains__(st):
                related_news.add(n)
    related_news = list(related_news)
    return related_news


def get_related_news_by_tag(news, *special_text):
    related_news = set([])
    for st in special_text:
        for n in news:
            for t in n.tag_set.all():
                if t.text.__contains__(st):
                    related_news.add(n)
    related_news = list(related_news)
    return related_news


def get_related_news_by_title(news, *special_text):
    related_news = set([])
    for st in special_text:
        for n in news:

            if n.title.__contains__(st):
                related_news.add(n)

    related_news = list(related_news)
    return related_news


def get_related_news_by_text(news, *special_text):
    related_news = set([])
    for st in special_text:
        for n in news:
            if n.text.__contains__(st):
                related_news.add(n)
    related_news = list(related_news)
    return related_news




def filter_games_by_winning_loosing(team_in_games, situation_text):
    games = []
    for tg in team_in_games:
        if tg.situation == situation_text:
            games.append(tg.game)
    return games


def get_related_news_to_game(news, *team_names):
    related_news = set([])

    for n in news:
        if n.text.__contains__(team_names[0]) and n.text.__contains__(team_names[1]):
            related_news.add(n)
        if n.title.__contains__(team_names[0]) and n.text.__contains__(team_names[1]):
            related_news.add(n)
    related_news = list(related_news)
    return related_news


def filter_leagues_by_text(leagues, special_text):
    filtered_leagues = []
    for l in leagues:
        league_complete_name = str(l)
        if league_complete_name.__contains__(special_text):
            filtered_leagues.append(l)
    return filtered_leagues


