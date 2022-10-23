import newsapi
import requests
from django.shortcuts import render
from newsapi import *


# Create your views here.
from newsapi.newsapi_client import NewsApiClient


def index(request):
    new_api = NewsApiClient(api_key='e969005bf4194ca78a2c972a90ca3bd8')
    hand_lines = new_api.get_top_headlines(sources='espn')
    articles = hand_lines['articles']
    description = []
    news = []
    image = []
    for i in range(len(articles)):
        article = articles[i]
        description.append(article['description'])
        news.append(article['title'])
        image.append(article['urlToImage'])
    list_news = zip(news, description, image)
    return render(request, "index.html" , context = {'news': list_news})

