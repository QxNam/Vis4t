from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Teacher
from django.forms import ModelForm
from django.core.exceptions import ValidationError
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

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_fullname', 'email', 'phone_number', 'year_of_birth', 'academic_title']
        widgets = {
            'teacher_fullname': forms.TextInput(attrs={'class': 'input-update'}),
            'email': forms.EmailInput(attrs={'class': 'input-update'}),
            'phone_number': forms.TextInput(attrs={'class': 'input-update'}),
            'year_of_birth': forms.TextInput(attrs={'class': 'input-update'}),
            'academic_title': forms.TextInput(attrs={'class': 'input-update'}),
            # 'sex': forms.RadioSelect(choices=(('M', 'Nam'), ('F', 'Nữ')))
        }
    