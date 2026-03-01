from django.http import JsonResponse
from django.shortcuts import render
from .models import TaxAdvice

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaxAdviceSerializer

@api_view(['GET'])
def tax_advice_api(request):

    category = request.GET.get('category')
    qs = TaxAdvice.objects.all()

    if category:
        qs = qs.filter(category=category)

    serializer = TaxAdviceSerializer(qs, many=True)

    return Response({
        "count": qs.count(),
        "tips": serializer.data,
    })


def tax_consultancy_page(request):

    latest_tips = TaxAdvice.objects.all()[:5]
    return render(request, "tax_consultancy.html", {
        "latest_tips": latest_tips,
    })