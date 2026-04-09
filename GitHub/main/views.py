import os
from django.shortcuts import render, redirect
from newsapi import NewsApiClient
from dotenv import load_dotenv
from .models import Post
load_dotenv()

# Create your views here.

def index(request):
    if request.method == "POST":
        Post.objects.all().delete()
       
    repos = Post.objects.all()
    newsapi = NewsApiClient(api_key=os.getenv('API_KEY'))
    top_headlines = newsapi.get_top_headlines(language='en')

    context = {'top_headlines': top_headlines['articles'][:5], 'repos': repos}
    return render(request, 'main/index.html', context=context)

def repo(request):
    if request.method == 'POST':
        title = request.POST.get('title', "").strip()
        description = request.POST.get('description', "").strip()
        if title and description:
            Post.objects.create(title=title, description=description)
            return redirect(index)
    return render(request, "main/repo.html")