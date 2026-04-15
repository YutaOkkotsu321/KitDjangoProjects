from django.urls import path
from main import views

urlpatterns = [
    path("", views.main),
    path("toggle/<int:pk>/", views.toggle_todo, name="toggle_todo")
]