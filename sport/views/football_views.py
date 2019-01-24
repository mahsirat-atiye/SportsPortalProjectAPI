from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from sport.models import News, FootballTeam
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
    team = get_object_or_404(FootballTeam, pk=team_id)
    related_news = []
    # نام
    # تیم
    # یا
    # بازیکنهای
    # تیم
    # در
    # عنوان - برچسبها - «
    # متن
    # خبر
    # وجود
    # دارد

    # just for rendering
    # todo
    news = News.objects.all()[0]
    related_news.append(news)

    context = {
        'team': team,
        'related_news': related_news
    }

    return render(request, 'sport/football_team_detail.html', context)
