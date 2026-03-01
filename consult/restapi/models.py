from django.db import models

class TaxAdvice(models.Model):
    CATEGORY_CHOICES = [
        ('income_tax', 'Income Tax'),
        ('gst', 'GST'),
        ('investment', 'Investment & Savings'),
        ('business_tax', 'Business Tax'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    short_tip = models.CharField(max_length=255)
    detailed_advice = models.TextField()
    country = models.CharField(max_length=100, default="India")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Tax Advice"
        verbose_name_plural = "Tax Advice"

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"