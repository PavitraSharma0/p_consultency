from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control bg-white border-0',
                'placeholder': 'Your Name',
                'style': 'height: 55px;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-white border-0',
                'placeholder': 'Your Email',
                'style': 'height: 55px;'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control bg-white border-0',
                'rows': 5,
                'placeholder': 'Comment'
            }),
        }