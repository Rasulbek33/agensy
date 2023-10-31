from django.shortcuts import render
from django.views.generic import TemplateView
from portfolio.models import Portfolio

class PortfolioView(TemplateView):
    model = Portfolio
    template_name = 'html/portfolio.html'