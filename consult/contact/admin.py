from django.contrib import admin
from .models import ContactMessage

# Register your models here.

@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('fullname', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    