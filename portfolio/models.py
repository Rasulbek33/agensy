from django.db import models

class Portfolio(models.Model):
    img  = models.ImageField(blank=True)
    title = models.CharField(max_length=255, blank=True)
    article = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'
