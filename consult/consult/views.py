from django.http import HttpResponse
from django.shortcuts import render
from ourservice.models import Service
from quote.forms import QuoteForm

def HomePage(request):
    serviceData = Service.objects.all()
    form = QuoteForm()
    
    data = {
        'serviceData': serviceData,
        'form': form,
    }
    return render(request, "index.html", data)
