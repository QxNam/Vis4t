from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Teacher, Class
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, './home/home.html')


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                teacher = Teacher.objects.get(login_name = username)
            except:
                teacher = None
            
            if teacher:
                if teacher.password == password:
                    context = {'user': teacher}
                    return render(request, './home/home.html', context=context)
            # print(t)
            # user = authenticate(request, username=username, password=password)
            
            messages.success(request, 'Tài khoản hoặc mật khẩu không đúng')
            redirect('login')
    return render(request, 'login/login_form.html', 
                  {'form': LoginForm})
