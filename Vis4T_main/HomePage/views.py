from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .forms import LoginForm
from .models import Student, Teacher, University_class
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
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
    return render(request, 'login/login_form.html', 
                  {'form': LoginForm})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("login")
        

class ClassList(APIView):   
    def get(self, request,  format=None):
        queryset = University_class.objects.all()
        
        serializer = University_classSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    
class ClassDetail(APIView):
    def get_object(self, pk: str):
        pk = pk.upper()
        try:
            return University_class.objects.get(class_name=pk)
        except University_class.DoesNotExist:
            raise Http404
    
    # @api_view(['GET'])
    def get(self, request, pk, format=None):
        class_ = self.get_object(pk)
        serializer = University_classSerializer(class_)
        return JsonResponse(serializer.data)
        
        
class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer