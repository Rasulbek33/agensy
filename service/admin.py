from django.contrib import admin
from service.models import Service

@admin.register(Service)
class Service(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)

