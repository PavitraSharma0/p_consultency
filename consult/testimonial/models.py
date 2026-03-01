from django.db import models

# Create your models here.

class Testimonial(models.Model):
    client_name = models.CharField(max_length=150)
    profession = models.CharField(max_length=100)
    comment = models.TextField()
    client_image = models.ImageField(upload_to='testimonials/')

    def __str__(self):
        return self.client_name
