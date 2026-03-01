from django import forms
from .models import QuoteRequest

class QuoteForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['fullname', 'email', 'service']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
        }
    