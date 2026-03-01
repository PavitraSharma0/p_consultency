from .models import Service

def services_context(request):
    services = Service.objects.all()
    return {'services': services}