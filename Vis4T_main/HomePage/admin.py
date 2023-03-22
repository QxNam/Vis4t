from django.contrib import admin

# Register your models here.
from .models import Teacher, Class

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'password')

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Class)