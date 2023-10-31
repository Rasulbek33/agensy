from django.contrib import admin
from about.models import About

@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ('about_title', 'article')
    list_display_links = ('about_title', 'article')