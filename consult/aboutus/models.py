from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=200, default="Welcome To T-CONSULTANCY")
    subtitle = models.CharField(max_length=300, default="Diam dolor diam ipsum sit. Clita erat ipsum et lorem stet no lorem sit clita duo justo magna dolore")
    description = models.TextField(default="Et stet ipsum nonumy rebum eos justo, accusam invidunt aliquyam stet magna at et sanctus, vero sea sit amet dolores, sit dolor duo invidunt dolor, kasd rebum consetetur diam invidunt erat stet.")
    quote_button_text = models.CharField(max_length=50, default="Get A Quote")

    # Right-side “service” sections
    service_1_title = models.CharField(max_length=100, default="Business Planning")
    service_1_description = models.TextField(default="Tempor erat elitr rebum at clita. Diam dolor ipsum amet eos erat ipsum lorem et sit sed stet lorem sit clita duo")
    service_1_icon = models.CharField(max_length=50, default="fa-user-tie")

    service_2_title = models.CharField(max_length=100, default="Financial Analysis")
    service_2_description = models.TextField(default="Tempor erat elitr rebum at clita. Diam dolor ipsum amet eos erat ipsum lorem et sit sed stet lorem sit clita duo")
    service_2_icon = models.CharField(max_length=50, default="fa-chart-line")

    service_3_title = models.CharField(max_length=100, default="Legal Advisory")
    service_3_description = models.TextField(default="Tempor erat elitr rebum at clita. Diam dolor ipsum amet eos erat ipsum lorem et sit sed stet lorem sit clita duo")
    service_3_icon = models.CharField(max_length=50, default="fa-balance-scale")

    def __str__(self):
        return self.title