from django.shortcuts import render
from django.views.generic import TemplateView
from team.models import Team
class TeamView(TemplateView):
    model = Team
    template_name = 'html/team.html'
 