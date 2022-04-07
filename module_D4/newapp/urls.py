from django.urls import path
from .views import NewsList, NewsDetailView, NewsSearch

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetailView.as_view()),
    path('search/', NewsSearch.as_view(), name='news_search'),
]
