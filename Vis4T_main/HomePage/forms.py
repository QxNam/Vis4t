from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Teacher
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username',
        widget=forms.TextInput(attrs={
            'class': 'input',
            'type': 'text',
            'placeholder': 'Mã số giáo viên',
            'autofocus': True,
            'required': 'required'
        })
    )
    
    password = forms.CharField(label='Password', 
        widget=forms.PasswordInput(attrs={
            'class': 'input password',
            'name': 'pass',
            'placeholder': 'Mật khẩu',
            'required': 'required'
        }),
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = False
        self.fields['password'].label = False

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_fullname' ,'email', 'year_of_birth', 'sex', 'academic_title', 'phone_number']
    # teacher_name = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         'class': 'input-update',
    #         'name': 'name',
    #     })
    # )
    # email = forms.CharField(
    #     widget=forms.EmailField(attrs={
    #         'class': 'input-update',
    #         'name': 'email'
    #     })
    # )
    # phone_number = forms.CharField(
    #     widget=forms.CharField(attrs={
    #         'class': 'input-update',
    #         'name': 'phone_number'
    #     })
    # )