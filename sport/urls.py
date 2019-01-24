from django.urls import path

from sport.views import recent_general_news, news_detail_view
from . import views

app_name = "sport"
urlpatterns = [

    path('last-ten-news/general/football', recent_general_news, name='last-ten'),
    path('<int:news_id>/news-detail', news_detail_view, name='news-detail'),

]
