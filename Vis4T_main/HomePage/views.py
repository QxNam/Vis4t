from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic.edit import UpdateView, CreateView
from django.core.cache import cache
from django.db.models import Q
from django.http import Http404, JsonResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .forms import *
from .models import Student, Teacher, University_class
from .serializers import *
from .utils import *
import json
# Create your views here.
    
class Login(LoginView):
    template_name = 'login/login_form.html'
    fields = ['username', 'password']
    redirect_authenticated_user = True
    authentication_form = LoginForm
    def get_success_url(self):
        class_ = University_class.objects.filter(teacher=self.request.user).first()
        class_name = class_.class_name if class_ else False
        return reverse_lazy('home', kwargs={'class_name': class_name})
    
    @staticmethod
    def send_gmail(request):
        if request.method == 'POST':
            gmail_value = request.POST.get('gmail')
            print(gmail_value)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error'})
        
class HomeView(LoginRequiredMixin, ListView):
    model = University_class
    context_object_name = 'classes'
    template_name = 'home/home.html'
    
    def returnHomeNone(self, context):
        self.template_name = 'home/homeNone.html'
        context['cached_class_name'] = None
        context['current_link'] = 'home'
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
        if class_name:
            
            university_class = University_class.objects.filter(teacher=self.request.user).first()
            if university_class is None:
                return self.returnHomeNone(context)
                
            context['class'] = university_class
            cached_class_name = cache.get('class_name')
            if cached_class_name == class_name:
                context['cached_class_name'] = cached_class_name
            else:
                context['cached_class_name'] = university_class.class_name
                cache.set('class_name', university_class.class_name)
                
            subject_class_list = list(Subject_class.objects.filter(class_name=university_class).values())
            student_list = list(Student.objects.filter(class_name=university_class).order_by('-score_10').values())
            if len(student_list) == 0:
                return self.returnHomeNone(context)
            
            for i in range(len(student_list)):
                student_list[i]['ranking'] = i + 1
            context['student_list'] = student_list
            context['student'] = context['student_list'][0]
            context['subject'] = subject_class_list
            context['first_subject'] = subject_class_list[0]
        else:
            return self.returnHomeNone(context)
            
        context['current_link'] = 'home'
        return context
    
    def class_home(self):
        return self.render_to_response(self.get_context_data())   
class AddNewClass(LoginRequiredMixin, CreateView):
    model = Teacher
    template_name = 'addClass/addNewClass.html'
    context_object_name = 'teacher'
    form_class = UniversityClassForm
    
    success_url = reverse_lazy('upload_file')
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
        class_.save()        
        cache.set('uploading_class', class_.class_name)
        return super().form_valid(form)
class UploadFile(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'addClass/upload_file.html'
    context_object_name = 'teacher'
    def get_queryset(self):
        teacher = self.request.user
        return teacher
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = University_class.objects.filter(teacher=self.request.user)
        context['cached_class_name'] = cache.get('class_name')
        context['current_link'] = 'updateClass'
        context['uploading_class'] = cache.get('uploading_class')
        return context

@csrf_exempt
def update_cache(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        class_name = data['class_name']
        class_ = University_class.objects.filter(class_name=class_name).first()
        if class_ is None or class_.teacher != request.user:
            return JsonResponse({'status': False, 'message': 'Class not found.'}, status=404)
        cache.set('uploading_class', class_name)
        return JsonResponse({'status': True, 'message': 'Cache updated successfully.'})
    else:
        return JsonResponse({'status': False, 'message': 'Invalid request method.'}, status=400)

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
        