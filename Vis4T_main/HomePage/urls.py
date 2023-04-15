from . import views
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    # path('router', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),
    
    path('login/', views.Login.as_view(), name="login"),
    path('home/', views.HomeView.as_view(), name="home"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    
    path('course/', views.course_overview, name='course'),
    path('class/', views.ClassList.as_view(), name='class_api'),
    path('class_list/', views.ClassListDetail.as_view(), name='class_list_api'),
    path('class_list/<str:pk>', views.ClassListDetail.as_view(), name='class_list_api'),
    
    path('class/<str:pk>/', views.ClassDetail.as_view(), name='class_detail_api'),
    
    
    path('teacher/<str:pk>', views.TeacherDetail.as_view(), name='teacher_api'),
    path('student/', views.StudentView.as_view(
        {'get': 'list', 'post': 'create'}), name='student_api'),
    # path('student/<str:pk>/', views.StudentDetail.as_view(), name='student_detail_api'),
])
