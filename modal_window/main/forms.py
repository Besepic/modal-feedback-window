from django import forms
from .models import Modal
from django.forms import TextInput

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Modal
        fields = ['name', 'phone', 'email']
        widgets = {
                'name': TextInput(attrs={
                    'class': 'form-control', 
                    'placeholder': 'Enter your name',
                    'type': "text",
                    'id': "name"
                }),
                'phone': TextInput(attrs={
                    'class': 'form-control', 
                    'placeholder': 'Enter your phone number',
                    'type': "tel",
                    'id': "phone"
                }),
                'email': TextInput(attrs={
                    'class': 'form-control', 
                    'placeholder': 'Enter your email',
                    'type': "email",
                    'id':"email" 
                }),
            }