import os
from django.shortcuts import render, redirect, get_object_or_404
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
    repos = Post.objects.all()
    context = {'repos': repos}
   
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'clean-btn':
            Post.objects.all().delete()
            return redirect(index)
        elif action == 'add-btn':
            title = request.POST.get('title', "").strip()
            description = request.POST.get('description', "").strip()
            if title and description:
                Post.objects.create(title=title, description=description)
                return redirect(index)
    return render(request, "main/repo.html", context=context)
def repo_detail(request, pk):
    repos = Post.objects.all()
    repo = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        Post.objects.all().delete()
        return redirect(index)
    return render(request, "main/repo_detail.html", context={'repo': repo, 'repos': repos})
