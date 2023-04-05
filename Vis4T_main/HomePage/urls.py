from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()
# router.register(r'class', views.ClassView)
# router.register(r'teacher', views.TeacherView)
# router.register(r'student', views.StudentView)


urlpatterns = format_suffix_patterns([
    # path('router', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('home/', auth_views.LoginView.as_view(template_name='./home/home.html'), name='home'),
    path('course/', views.course_overview, name='course'),
    path("logout", views.logout_request, name= "logout"),

    
    path('class/', views.ClassList.as_view(), name='class_api'),
    path('class/<str:pk>/', views.ClassDetail.as_view(), name='class_detail_api'),
    path('teacher/<str:pk>', views.TeacherDetail.as_view(), name='teacher_api'),
    path('student/', views.StudentView.as_view(
        {'get': 'list', 'post': 'create'}), name='student_api'),
    # path('student/<str:pk>/', views.StudentDetail.as_view(), name='student_detail_api'),
])
