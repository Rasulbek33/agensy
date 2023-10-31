from django.shortcuts import render
from django.views.generic import TemplateView
from service.models import Service

class ServiceView(TemplateView):
    model = Service
    template_name = 'html/services.html'
