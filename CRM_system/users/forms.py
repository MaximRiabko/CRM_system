from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegisterCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'surname', 'last_name', 'password1', 'password2', 'phone',]
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone': 'Телефон',
            'surname': 'Отчество',
        }

        widgets = {
            'email': forms.TextInput(attrs={'class': 'input-text'}),
            'first_name': forms.TextInput(attrs={'class': 'input-text'}),
            'last_name': forms.TextInput(attrs={'class': 'input-text'}),
            'phone': forms.TextInput(attrs={'class': 'input-text'}),
            'surname': forms.TextInput(attrs={'class': 'input-text'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email