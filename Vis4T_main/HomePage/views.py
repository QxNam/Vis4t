from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm
from .models import Teacher, University_class
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request, teacher, classes):
    context = {'teacher': teacher, 'classes': classes}
    return render(request, './home/home.html', context=context)

        
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            teacher = Teacher.objects.get(username=username)
            classes = University_class.objects.filter(teacher=teacher)
            print(len(classes))
            return home(request, teacher, classes)
            # return render(request, 'home/home.html', context={'teacher': teacher})
    return render(request, 'login/login_form.html', 
                  {'form': LoginForm})
