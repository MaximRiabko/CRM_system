from django.forms import ModelForm
from django import forms
from .models import Service

class ServiceCreationForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price']
        labels = {
            'name': 'Название',
            'description': 'описание',
            'price': 'цена'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-text'}),
            'description': forms.Textarea(attrs={'class': 'textarea_service', 'style': 'resize:none'}),
            'price': forms.TextInput(attrs={'class': 'input-text'}),
        }