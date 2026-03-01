from django.db import models

# Create your models here.
class TeamMember(models.Model):
    fullname = models.CharField(max_length=150)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team_photos/')
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return self.fullname
