from django.contrib import admin

# Register your models here.
from .models import Teacher, University_class, Student


admin.site.register(Teacher)
admin.site.register(University_class)
admin.site.register(Student)