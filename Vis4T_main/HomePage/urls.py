from . import views
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('', views.Login.as_view(), name="login"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    
    path('home/<str:class_name>/', views.HomeView.as_view(class_home=True), name='home'),
    path('student/<str:student_id>/', views.StudentView.as_view(), name='student_view'),
    
    
    path('class_list/<str:pk>', views.ClassListDetail.as_view(), name='class_list_api'),
    
    path('class/<str:pk>/', views.ClassDetail.as_view(), name='class_detail_api'),
    path('student/', views.StudentSubjectDetail.as_view(), name = "student_subject_api"),
    path('subject/', views.SubjectStudentDetail.as_view(), name = "subject_api"),
    path('add_class/', views.AddNewClass.as_view(), name = "add_class"),
    path('upload_file/<str:class_name>', views.UploadFile.as_view(), name = "upload_file"),
    path('subject_confirm/<str:class_name>', views.Subject_confirm.as_view(), name = "subject_confirm"),
    path('teacher/', views.TeacherView.as_view(), name = "teacher"),
    path('teacher/teacher_update/', views.TeacherUpdate.as_view(), name = "teacher_update"),
                                                   
    path('autocomplete/', views.AutocompleteStudent.as_view(), name='autocomplete'),
    path('about_us/H2', views.AboutUS.as_view(), name = "about_us"),
    
    path('add_note_class/', views.AddClassNote.as_view(), name = "add_note_class"),
    
    path('reset_password/', views.PasswordReset.as_view(), name='reset_password'),
    path('reset_password_sent/', views.PasswordResetSent.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
])
