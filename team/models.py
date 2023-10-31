from django.db import models

class Team(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    img = models.ImageField(blank=True)
    name = models.CharField(max_length=255, blank=True)
    name_title = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
