from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    img = models.ImageField(blank=True)
    article = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'