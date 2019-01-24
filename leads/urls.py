from django.urls import path
from . import views

urlpatterns = [

    path('api/lead/', views.LeadListCreate.as_view()),
    path('api/news/', views.NewsCreate.as_view()),
    path('test/image', views.test_image)

]