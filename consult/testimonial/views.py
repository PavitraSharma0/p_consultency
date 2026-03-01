from django.shortcuts import render
from .models import Testimonial

# Create your views here.
def testimonial_view(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonial.html', {'testimonials': testimonials})
