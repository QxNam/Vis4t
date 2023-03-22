from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('home/', auth_views.LoginView.as_view(template_name='./home/home.html'), name='home'),
]