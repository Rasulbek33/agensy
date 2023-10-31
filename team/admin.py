from django.contrib import admin
from team.models import Team

@admin.register(Team)
class Team(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
