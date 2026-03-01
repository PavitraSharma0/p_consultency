from django.shortcuts import render
from .models import Service

# Create your views here.
def service_page(request):
    services = Service.objects.all()
    return render(request, 'service.html', {'services': services})
