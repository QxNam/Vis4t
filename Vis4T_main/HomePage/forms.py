from django import forms
from django.contrib.auth.forms import AuthenticationForm
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username',
        widget=forms.TextInput(attrs={
            'class': 'input',
            'type': 'text',
            'placeholder': 'Tài khoản *',
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = False
        self.fields['password'].label = False