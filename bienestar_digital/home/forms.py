from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.text import capfirst

class LoginForm(AuthenticationForm):
    next = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'next'})
    )
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=request, *args, **kwargs)
        self.fields['username'].label = 'Usuario/Identificación'
        self.fields['password'].label = 'Contraseña'


class RegistryForm(forms.Form):
    username = forms.CharField(
        label='Identificación y Usuario:',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username'})
    )
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password1'})
    )
    password2 = forms.CharField(
        label='Confirmación de contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password2'})
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")