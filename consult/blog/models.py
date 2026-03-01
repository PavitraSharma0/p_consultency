from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, default="Admin")
    category = models.CharField(max_length=100, default="General")
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']

class Comment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.blog.title}"