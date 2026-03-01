from django.db import models

# Create your models here.

class Service(models.Model):
    service_title = models.CharField(max_length= 150)
    service_desc = models.TextField()
    service_read_link = models.CharField(max_length= 150, blank=True)
    service_icon = models.CharField(max_length=150, default='fa-cog', help_text='fa-chart-line')

    def __str__(self):
        return self.service_title
