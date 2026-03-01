from rest_framework import serializers
from .models import TaxAdvice

class TaxAdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxAdvice
        fields = [
            'id',
            'title',
            'category',
            'short_tip',
            'detailed_advice',
            'country',
            'created_at',
            ]