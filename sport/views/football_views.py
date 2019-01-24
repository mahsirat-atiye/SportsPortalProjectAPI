from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from sport.models import News
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
