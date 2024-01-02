from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}),
        required=True
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}),
        required=True
    )
    next = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'next'})
    )


class RegistryForm(forms.Form):
    username = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'username'})
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