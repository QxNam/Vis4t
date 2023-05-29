from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from .models import Teacher, University_class
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
            'phone_number': forms.TextInput(attrs={'class': 'input-update'}),
            'year_of_birth': forms.TextInput(attrs={'class': 'input-update'}),
            'academic_title': forms.TextInput(attrs={'class': 'input-update'}),
            # 'email': forms.EmailInput(attrs={'class': 'input-update'}),
            # 'sex': forms.RadioSelect(choices=(('M', 'Nam'), ('F', 'Nữ')))
        }
class UniversityClassForm(ModelForm):
    class Meta:
        model = University_class
        fields = ['class_name', 'class_major', 'total_credit', 'total_semester']
        labels = {
            'class_name': 'Tên lớp *',
            'class_major': 'Chuyên ngành *',
            'total_credit': 'Tổng số tín chỉ *',
            'total_semester': 'Tổng số học kì *',
        }
        widgets = {
            'class_name': forms.TextInput(attrs={'class': 'form-control'}),
            'class_major': forms.TextInput(attrs={'class': 'form-control'}),
            'total_credit': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_semester': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['class_name'].widget.attrs['placeholder'] = '( VD: KHDL16A, KHMT15BTT ... )'
        self.fields['class_major'].widget.attrs['placeholder'] = '( VD: Khoa học dữ liệu, Khoa Học Máy Tính ... )'
        self.fields['total_credit'].widget.attrs['placeholder'] = '( Ví dụ: 100, 120,... )'
        self.fields['total_semester'].widget.attrs['placeholder'] = '( VD: 9, 8,... ) (Tối đa 9 học kì)'
    
class GmailForm(PasswordResetForm):
    email = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={
                'type': 'email',
                'name': 'gmail',
                'class': 'input',
                'placeholder': 'Nhập email *',
                'autofocus': 'autofocus',
                'required': 'required',
                'maxlength': '150',
                'id': 'gmail',
            }
        )
    )
    class Meta:
        model= Teacher
        fields = ['email']
    
    