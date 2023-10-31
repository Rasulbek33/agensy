from django.contrib import admin
from main.models import Home

@admin.register(Home)
class Home(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)

