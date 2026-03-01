from django import forms
from .models import StayUpdate

class StayUpdateForm(forms.ModelForm):
    class Meta:
        model = StayUpdate
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control border-white p-3','placeholder': 'Your Email',}),
        }
        