from django import forms
from django.contrib.auth.forms import AuthenticationForm
class LoginForm(forms.Form):
    username = forms.CharField(label='Username',
        widget=forms.TextInput(attrs={
            'class': 'input',
            'type': 'text',
            'placeholder': 'Tài khoản *', #max_length=100,
            'autofocus': True,
            'required': 'required'
        })
    )
    password = forms.CharField(label='Password', 
        widget=forms.PasswordInput(attrs={
            'class': 'input password',
            'name': 'pass',
            'placeholder': 'Mật khẩu *',
            'required': 'required'
        }),
    )
    