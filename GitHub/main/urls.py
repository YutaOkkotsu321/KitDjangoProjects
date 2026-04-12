from django.urls import path
from main import views

urlpatterns = [
    path("", views.index, name='index'),
    path("addrepo/", views.repo, name='repo'),
    path("repo/<int:pk>/", views.repo_detail, name="repo_detail")
]