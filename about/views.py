from django.shortcuts import render
from django.views.generic import TemplateView
from about.models import About

class AboutView(TemplateView):
    model = About
    template_name = 'html/About.html'
