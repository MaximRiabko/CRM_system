from django.forms import ModelForm
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
