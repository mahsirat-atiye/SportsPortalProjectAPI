from http.client import HTTPResponse

from django.shortcuts import render

from leads.models import Lead, News
from leads.serializers import LeadSerializer, NewsSerializer
from rest_framework import generics


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class NewsCreate(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


def test_image(request):
    news = News.objects.all()[0]
    return render(request, 'test.html', {"news": news})
