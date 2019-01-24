from django.views import generic

from sport.models import News
from django.utils import timezone


class RecentGeneralNews(generic.ListView):
    template_name = 'sport/recent_general_news.html'
    context_object_name = 'latest_news'

    def get_queryset(self):
        return News.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')[:10]
