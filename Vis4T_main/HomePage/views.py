from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm
from .models import Teacher, University_class, Student
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@login_required(login_url='login')
@csrf_protect 
def home(request, teacher, classes):
    students = Student.objects.filter(class_name=classes[2])
    print(students)
    context = {'teacher': teacher, 'classes': classes, 'students': students}
    return render(request, './home/home.html', context=context)

        
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                teacher = Teacher.objects.get(username=username)
                classes = University_class.objects.filter(teacher=teacher)
                return home(request, teacher, classes)
            else:
                messages.error(request, 'Tài khoản hoặc mật khẩu không đúng')
                redirect('login')
            # return render(request, 'home/home.html', context={'teacher': teacher})
    return render(request, 'login/login_form.html', 
                  {'form': LoginForm})
