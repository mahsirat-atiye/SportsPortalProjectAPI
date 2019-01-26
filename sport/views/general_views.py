from django.shortcuts import get_object_or_404, render
from django.views import generic

from sport.models import News, Comment


class NewsDetailView(generic.DetailView):
    template_name = 'sport/news_detail.html'
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

    return render(request, 'sport/news_detail.html', {
        'news': news,
        'related_news': related_news,
        "comments": comments

    }
                  )
