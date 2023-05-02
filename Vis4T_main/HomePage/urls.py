from . import views
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('', views.Login.as_view(), name="login"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('gmail/', views.Login.send_gmail, name='send_gmail'),
    
    path('home/<str:class_name>/', views.HomeView.as_view(class_home=True), name='home'),
    
    path('course/', views.course_overview, name='course'),
    path('class_list/<str:pk>', views.ClassListDetail.as_view(), name='class_list_api'),
    
    path('class/<str:pk>/', views.ClassDetail.as_view(), name='class_detail_api'),
    path('student/', views.StudentSubjectDetail.as_view(), name = "student_subject_api"),
    path('new_class/', views.AddNewClass.as_view(), name = "new_class"),
    path('teacher/', views.TeacherView.as_view(), name = "teacher"),
    path('teacher/teacher_update/', views.TeacherUpdate.as_view(), name = "teacher_update"),
    
    path('about_us/H2', views.AboutUS.as_view(), name = "about_us"),
])
