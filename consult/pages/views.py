from django.shortcuts import render
from feature.models import Feature

# Create your views here.
def blog_view(request):
    return render(request, 'blog.html')

def detail_view(request):
    return render(request, 'detail.html')

def feature_view(request):
    features = Feature.objects.all()
    return render(request, 'feature.html', {'features': features})

def quote_view(request):
    return render(request, 'quote.html')

def team_view(request):
    return render(request, 'team.html')

def testimonial_view(request):
    return render(request, 'testimonial.html')
