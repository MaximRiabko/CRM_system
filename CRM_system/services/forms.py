from django.forms import ModelForm
from django import forms
from .models import Service, AdvertisingСompany

class AdvertisingСompanyCreationForm(ModelForm):
    class Meta:
        model = AdvertisingСompany
        fields = ['company_name', 'advertised_service', 'promotion_channel', 'budget']
        labes = {
            'company_name': 'Название компании',
            'advertised_service': 'Рекламная услуга',
            'promotion_channel': 'Продвижение канала',
            'budget': 'Бюджет'
        }

        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'input-text'}),
            'advertised_service': forms.TextInput(attrs={'class': 'input-text'}),
            'promotion_channel': forms.TextInput(attrs={'class': 'input-text'}),
            'budget': forms.TextInput(attrs={'class': 'input-text'}),
        }

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