import os
from django.shortcuts import render
from newsapi import NewsApiClient
from dotenv import load_dotenv

load_dotenv()

# Create your views here.

def index(request):
    newsapi = NewsApiClient(api_key=os.getenv('API_KEY'))
    top_headlines = newsapi.get_top_headlines(language='en')

    context = {'top_headlines': top_headlines['articles'][:5]}
    return render(request, 'main/index.html', context=context)