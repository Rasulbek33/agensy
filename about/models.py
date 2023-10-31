from django.db import models

class About(models.Model):
    about_title = models.CharField(max_length=255, blank=True)
    img = models.ImageField(blank=True)
    article = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.about_title
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'