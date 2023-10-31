from django.urls import path
from main.views import HomeView


urlpatterns = [
    path('home/', HomeView.as_view()),
]