from django.db import models

# Create your models here.
class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='fa-cog', help_text='fa-chart-line')

    def __str__(self):
        return self.title