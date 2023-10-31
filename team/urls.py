from django.urls import path
from team.views import TeamView


urlpatterns = [
    path('home/', TeamView.as_view()),
]