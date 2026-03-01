from django.shortcuts import render
from ourservice.models import Service
from feature.models import Feature
from testimonial.models import Testimonial
from aboutus.models import AboutUs
from blog.models import Blog
from stayupdate.forms import StayUpdateForm

# Create your views here.

def home_view(request):
    services = Service.objects.all()
    features = Feature.objects.all()
    testimonials = Testimonial.objects.all()
    about = AboutUs.objects.first()
    blogs = Blog.objects.all().order_by('-date')[:3]
    form = StayUpdateForm()
    return render(request, 'index.html', {'services': services,'features': features, 'testimonials': testimonials,'about': about, 'blogs': blogs, 'form':form})