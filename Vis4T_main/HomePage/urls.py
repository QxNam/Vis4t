from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('home/', auth_views.LoginView.as_view(template_name='./home/home.html'), name='home'),
    path("logout", views.logout_request, name= "logout"),
]