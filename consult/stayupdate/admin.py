from django.contrib import admin
from .models import StayUpdate

# Register your models here.
@admin.register(StayUpdate)
class StayUpdateAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('email',)
    readonly_fields = ('created_at',)
