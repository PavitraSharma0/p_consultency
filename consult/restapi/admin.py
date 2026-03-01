from django.contrib import admin
from .models import TaxAdvice

@admin.register(TaxAdvice)
class TaxAdviceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'country', 'created_at')
    list_filter = ('category', 'country', 'created_at')
    search_fields = ('title', 'short_tip', 'detailed_advice')