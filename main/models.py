from django.db import models

class Home(models.Model):
    banner = models.ImageField(upload_to='media/banner/%Y/%m/%d')
    title = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'
