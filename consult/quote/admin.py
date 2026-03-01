from django.contrib import admin
from .models import QuoteRequest

# Register your models here.

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'service', 'created_at')
    search_fields = ('fullname', 'email', 'service')
    readonly_fields = ('created_at',)
