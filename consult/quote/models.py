from django.db import models

# Create your models here.

class QuoteRequest(models.Model):
    SERVICE_CHOICES = [
        ('Financial Consultancy', 'Financial Consultancy'),
        ('Strategy Consultancy', 'Strategy Consultancy'),
        ('Tax Consultancy', 'Tax Consultancy'),
    ]
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Quote Request'
        verbose_name_plural = 'Quote Requests'

    def __str__(self):
        return f"{self.fullname} - {self.service}"
