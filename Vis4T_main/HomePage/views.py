from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from .forms import LoginForm
from .models import Student, Teacher, University_class
from .serializers import *
from .utils import *

# Create your views here.
    
class Login(LoginView):
    template_name = 'login/login_form.html'
    fields = ['username', 'password']
    redirect_authenticated_user = True
    authentication_form = LoginForm
    success_url = reverse_lazy('home')
    

class HomeView(LoginRequiredMixin, ListView):
    model = University_class
    template_name = 'home/home.html'
    context_object_name = 'classes'
    
    def get_queryset(self):
        teacher = self.request.user
        queryset = super().get_queryset()
        queryset = queryset.filter(teacher__teacher_id=teacher.teacher_id)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher'] = self.request.user
        return context
class TeacherView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teacher/teacher.html'
    context_object_name = 'teacher'
    
    def get_queryset(self):
        teacher = self.request.user
        return teacher
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = University_class.objects.filter(teacher=self.request.user)
        return context



class ClassList(APIView):   
    def get(self, request,  format=None):
        queryset = University_class.objects.all()
        serializer = University_classSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

class ClassDetail(APIView):
    def get_object(self, pk: str):
        try:
            return University_class.objects.get(class_name=pk)
        except University_class.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        pk = pk.upper()
        class_ = self.get_object(pk)
        class_serializer = University_classSerializer(class_)
        student_ = Student.objects.filter(class_name=class_)
        student_serializer = StudentSerializer(student_, many=True)
        student_data = student_serializer.data
        
        response = {
            'class_info': class_serializer.data, 
            'score_char_data': query_student_data_with_ordinal_data(student_data, 'score_char')['count'],
            'rank_data': query_student_data_with_ordinal_data(student_data, 'rank')['count'],
            'score10_data': get_student_final_score(student_data),
            'score4_data': get_student_final_score(student_data, 'score_4')
        }
        return JsonResponse({'data': response}, safe=False)
class ClassListDetail(APIView):
    def get_object(self, pk: str):
        try:
            return University_class.objects.get(class_name=pk)
        except University_class.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        pk = pk.upper()
        class_ = self.get_object(pk)
        student = Student.objects.filter(class_name=class_)
        student_serializer = StudentSerializer(student, many=True)
        response = {'student': student_serializer.data}
        return JsonResponse(response, safe=False)       
        
class TeacherDetail(APIView):
    def get_object(self, pk: str):
        try:
            return Teacher.objects.get(teacher_id=pk)
        except Teacher.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        teacher = self.get_object(pk)
        teach_serializer = TeacherSerializer(teacher)
        class_ = University_class.objects.filter(teacher=teacher)
        class_serializer = University_classSerializer(class_, many=True)
        response = {
            "teacher": teach_serializer.data,
            "class": class_serializer.data
        }
        return JsonResponse(response, safe=False)

class StudentView( APIView):
    def get(self, request, class_name, format=None):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    
class StudentDetail(APIView):
    def get_object(self, pk: str):
        try:
            return Student.objects.get(student_id=pk)
        except Student.DoesNotExist:
            raise Http404
    
    # @api_view(['GET'])
    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)
class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
@login_required(login_url='login')
@csrf_protect 
def course_overview(request):
    return render(request, './course/course_overview.html')