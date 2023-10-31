from django.contrib import admin
from portfolio.models import Portfolio

@admin.register(Portfolio)
class Portfolio(admin.ModelAdmin):
    list_display = ('title', 'article' ,)
    list_display_links = ('title', 'article' ,)