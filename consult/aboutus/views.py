from django.shortcuts import render
from .models import AboutUs

# Create your views here.
def about_view(request):
    about = AboutUs.objects.first()
    return render(request, 'about.html', {'about': about})
