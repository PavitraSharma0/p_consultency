from django.contrib import admin
from .models import Blog, Comment

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'date')
    search_fields = ('title', 'author', 'category')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'blog', 'created_at')
    search_fields = ('name', 'email', 'content')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
