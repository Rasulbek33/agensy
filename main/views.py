from django.shortcuts import render
from django.views.generic import TemplateView
from main.models import Home
class HomeView(TemplateView):
    model = Home
    template_name = 'html/home.html'
 