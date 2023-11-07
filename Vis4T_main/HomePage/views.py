from datetime import datetime
from typing import Any
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.core.cache import cache
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from rest_framework import generics
from rest_framework.views import APIView

from .forms import *
from .models import Student, Teacher, University_class
from .serializers import *
from .utils import *

# Create your views here.
    
class Login(LoginView):
    template_name = 'login/login_form.html'
    fields = ['username', 'password']
    redirect_authenticated_user = True
    form_class = LoginForm
    def get_success_url(self):
        class_ = University_class.objects.filter(teacher=self.request.user, is_active=True).first()
        class_name = class_.class_name if class_ else False
        return reverse_lazy('home', kwargs={'class_name': class_name})

    
    
    
class HomeView(LoginRequiredMixin, ListView):
    model = University_class
    context_object_name = 'classes'
    template_name = 'home/home.html'
    def handle_no_permission(self):
         # pass None to redirect_field_name in order to remove the next param
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), None)
    def returnHomeNone(self, context, situation):
        self.template_name = 'home/homeNone.html'
        context['cached_class_name'] = None
        context['current_link'] = 'home'
        context['situation'] = situation
        return context
    
    def get_queryset(self):
        teacher = self.request.user
        queryset = super().get_queryset()
        queryset = queryset.filter(teacher__teacher_id=teacher.teacher_id)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher'] = self.request.user
        class_name = self.kwargs['class_name']
        if class_name is not None:
            university_class = University_class.objects.filter(class_name=class_name)
            if university_class.first() is None:
                university_class = University_class.objects.filter(teacher=self.request.user).first()
            else :
                university_class = university_class.first()
            if university_class.teacher != self.request.user:
                raise Http404
            
            
            context['class'] = university_class
            subject_class_list = Subject_class.objects.filter(class_name=university_class, semester_id__isnull=False)
            student_list = list(Student.objects.filter(class_name=university_class).order_by('-score_10').values())
            if len(student_list) == 0:
                return self.returnHomeNone(context, situation='zero_student')
            if len(subject_class_list) == 0:
                return self.returnHomeNone(context, situation='zero_subject')
            
            
        else:
            return self.returnHomeNone(context, situation='zero_class')
        context['class'] = university_class
        cached_class_name = cache.get('class_name')
        if cached_class_name == class_name:
            context['cached_class_name'] = cached_class_name
        else:
            context['cached_class_name'] = university_class.class_name
            cache.set('class_name', university_class.class_name)
            cached_class_name = cache.get('class_name')
        subject_class_list = list(subject_class_list.values())
        for i in range(len(student_list)):
            student_list[i]['ranking'] = i + 1
            
        context['student_list'] = student_list  
        context['subject'] = subject_class_list
        context['first_subject'] = subject_class_list[0]
        context['class_note'] = Note_class.objects.filter(class_name=cached_class_name) 
        context['current_link'] = 'home'
        context['current_date'] = datetime.now().strftime("%d/%m/%Y")
        return context
    
    def class_home(self):
        return self.render_to_response(self.get_context_data())  
    
class StudentView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'student/student.html'
    context_object_name = 'student'
    
    def get_queryset(self):
        teacher = self.request.user
        return teacher
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher'] = self.request.user
        
        context['classes'] = University_class.objects.filter(teacher=self.request.user)
        context['cached_class_name'] = cache.get('class_name')
        context['current_link'] = 'home'
        
        student_id = self.kwargs['student_id']
        context['student'] = Student.objects.get(student_id=student_id)
        context['class'] = University_class.objects.get(class_name = context['student'].class_name)     
        
        # check if this class is possed by this teacher
        if context['class'].teacher != self.request.user:
            raise Http404
        
        student_list = list(Student.objects.filter(class_name=context['class']).order_by('-score_10').values())
        for i in range(len(student_list)):
            student_list[i]['ranking'] = i + 1
        context['student_list'] = student_list
        
        subject = Subject_student.objects.filter(student_id=student_id)\
            .values("subject__subject_name", "subject__credit", "score_10")
        context['subject_list'] = list(subject)
        
        context['notes'] = Note_student.objects.filter(student_id=student_id)
        context['current_date'] = datetime.now().strftime("%d/%m/%Y")
        return context 
class AddNewClass(LoginRequiredMixin, CreateView):
    model = Teacher
    template_name = 'addClass/addNewClass.html'
    context_object_name = 'teacher'
    form_class = UniversityClassForm
    
    def get_queryset(self):
        teacher = self.request.user
        return teacher
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['classes'] = University_class.objects.filter(teacher=self.request.user)
        context['cached_class_name'] = cache.get('class_name')
        context['form'] = self.form_class()
        context['current_link'] = 'addNewClass'
        return context
    def form_valid(self, form):
        class_ = form.save(commit=False)
        class_.teacher = self.request.user
        class_.is_done = False
        class_.save()        
        self.success_url = reverse_lazy('upload_file', kwargs={'class_name': class_.class_name})
        return super().form_valid(form)
    
class UploadFile(LoginRequiredMixin, ListView):
    model = University_class
    template_name = 'addClass/upload_file.html'
    context_object_name = 'classes'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        class_ = University_class.objects.filter(class_name=self.kwargs['class_name']).first()
        if class_ is None:
            raise Http404
        context['teacher'] = self.request.user
        if class_.teacher != context['teacher']:
            raise Http404
        context['uploading_class'] = self.kwargs['class_name']
        
        
        context['classes'] = University_class.objects.filter(teacher=self.request.user)
        context['cached_class_name'] = cache.get('class_name')
        context['current_link'] = 'updateClass'
        
        return context

    def post(self, request, *args, **kwargs):
        class_name = self.kwargs['class_name']
        file = request.FILES.get('file')
        if file:
            class_ = University_class.objects.get(class_name=class_name)
            processor = DataProcessor(file)
            processor.get_all_student_detail(class_)
               
            
            return HttpResponseRedirect(f'/upload_file/{class_name}')  

        # File upload error occurred
        file_error = 'Please select a file.'
        context = self.get_context_data(**kwargs)
        context['file_error'] = file_error
        return self.render_to_response(context) 

class TeacherView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teacher/teacher.html'
    context_object_name = 'teacher'
    
    def get_queryset(self):
        teacher = self.request.user
        return teacher
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['graduate_classes'] = University_class.objects.filter(teacher=self.request.user, is_active=False)
        context['undergraduate_classes'] = University_class.objects.filter(teacher=self.request.user, is_active=True)
        context['classes'] = context['undergraduate_classes']
        context['cached_class_name'] = cache.get('class_name')
        context['current_link'] = 'teacher'

        return context
class TeacherUpdate(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacher/teacher_info_update.html'
    success_url = reverse_lazy('teacher')
    
    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = University_class.objects.filter(teacher=self.request.user)
        context['cached_class_name'] = cache.get('class_name')
        return context
    def form_valid(self, form):
        teacher = self.get_object()
        
        teacher.teacher_fullname = form.cleaned_data['teacher_fullname']
        
        teacher.phone_number = form.cleaned_data['phone_number']
        teacher.year_of_birth = form.cleaned_data['year_of_birth']
        teacher.academic_title = form.cleaned_data['academic_title']
        teacher.save()
        
        return super().form_valid(form)
class Subject_confirm(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'addClass/subject-confirm.html'
    
    context_object_name = 'teacher'
    
    def get_queryset(self):
        teacher = self.request.user
        return teacher
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = University_class.objects.filter(teacher=self.request.user)
        context['cached_class_name'] = cache.get('class_name')
        context['current_link'] = 'aboutus'
        
        return context
class AboutUS(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'about_us.html'
    
    context_object_name = 'teacher'
    
    def get_queryset(self):
        teacher = self.request.user
        return teacher
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = University_class.objects.filter(teacher=self.request.user)
        context['cached_class_name'] = cache.get('class_name')
        context['current_link'] = 'aboutus'
        
        return context
    
    

# API Views
class AddClassNote(APIView):
    def post(self, request):
        class_name = cache.get('class_name')
        date = datetime.now()
        class_ = University_class.objects.get(class_name=class_name)
        
        note = request.data.get('note')
        try:
            Note_class.objects.create(class_name=class_, content=note, name=date)
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'error'})

class DeleteClassNote(APIView):
    def delete(self, request, note_id):
        try:
            note = Note_class.objects.get(id=note_id)
            note.delete()
            return JsonResponse({'status': 'success'})
        except Note_class.DoesNotExist:
            return JsonResponse({'status': 'error'})
class UpdateClassNote(APIView):
    def put(self, request, note_id):
        try:
            note = Note_class.objects.get(id=note_id)
            note.content = request.data.get('note')
            note.save()
            return JsonResponse({'status': 'success'})
        except Note_class.DoesNotExist:
            return JsonResponse({'status': 'error'})

class AddStudentNote(APIView):
    def post(self, request):
        date = datetime.now()
        note = request.data.get('note')
        student = Student.objects.get(student_id=request.data.get('student_id'))
        try:
            Note_student.objects.create(student=student, content=note, name=date)
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'error'})
class DeleteStudentNote(APIView):
    def delete(self, request, note_id):
        try:
            note = Note_student.objects.get(id=note_id)
            note.delete()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            print(e)
            return JsonResponse({'status': 'error'})
class UpdateStudentNote(APIView):
    def put(self, request, note_id):
        try:
            note = Note_student.objects.get(id=note_id)
            note.content = request.data.get('note')
            note.save()
        except Exception as e:
            print(e)
            return JsonResponse({'status': 'error'})
    
    
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
        score10_data = get_student_final_score(student_data)
        response = {
            'class_info': class_serializer.data, 
            'score_char_data': query_student_data_with_ordinal_data(student_data, 'score_char')['count'],
            'rank_data': query_student_data_with_ordinal_data(student_data, 'rank')['count'],
            'score10_data': score10_data,
            'score4_data': get_student_final_score(student_data, 'score_4'),
            # 'kde_line_data': kde_line(score10_data, 0.1)
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
    

class StudentSubjectDetail(APIView):
    def get_object(self, student_id: str):
        try:
            return Student.objects.get(student_id=student_id)
        except Student.DoesNotExist:
            raise Http404
    def get(self, request):
        ENGLISH1 = "2111250"
        ENGLISH2 = "2111300"
        TOEIC = '2199450'
        student_id = request.query_params.get('student_id')
        if not student_id:
            raise Http404
        student = self.get_object(student_id)
        subjects = Subject_student.objects\
            .filter(student = student)\
            .exclude(subject_id = ENGLISH1)\
            .exclude(subject_id = ENGLISH2)\
            .exclude(subject_id = TOEIC)\
            .values(
                'subject__subject_name', 
                'subject__subject_id',
                'subject__credit',
                'score_10'
            )
        subjects = subjects.exclude(score_10__isnull=True).order_by('-score_10')
        english = Subject_student.objects.filter(student = student).filter(Q(subject_id = ENGLISH1) | Q(subject_id = ENGLISH2) | Q(subject_id = TOEIC)).values()
        res = {
            'subject_score':list(subjects),
            'english_score':list(english)
        }
        return JsonResponse(res, safe=False)

class SubjectStudentDetail(APIView):
    def get(self, request):
        subject_id = request.query_params.get('subject')
        class_ = request.query_params.get('class').upper()
        
        queryset = Student.objects.filter(class_name=class_).filter(subject_student__subject_id=subject_id)\
            .values('student_id', 'student_name', 'rank' , 'subject_student__score_10')
        queryset = list(queryset)
        for q in queryset:
            q['score_10'] = float(q['subject_student__score_10'])
            del q['subject_student__score_10']
        subject_name = Subject.objects.get(subject_id=subject_id).subject_name
    
        return JsonResponse({"subject_name": subject_name, "data": queryset}, safe=False)

class AutocompleteStudent(APIView):
    
    def get(self, request):
        letter = request.GET.get('letter')
        user = self.request.user
        classes = University_class.objects.filter(teacher=user)
        
        result = []
        for c in classes:
            students = Student.objects.filter(class_name=c, lastname__istartswith=letter).order_by('lastname')
            result += list(students.values('class_name', 'student_name', 'student_id'))

        return JsonResponse({'students': result}, safe=False)

# Password reset
class PasswordReset(PasswordResetView):
    template_name = 'login/password-reset.html'
    form_class = GmailForm
    
class PasswordResetSent(PasswordResetDoneView):
    template_name = 'login/password-reset-sent.html'
class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'login/password-reset-form.html'
    success_url = reverse_lazy('password_reset_complete')
    
    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        context['reset_confirm'] = True
        return context
    
class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'login/password-reset-done.html'