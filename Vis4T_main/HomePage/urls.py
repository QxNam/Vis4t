from . import views
from django.urls import path, include


app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
]