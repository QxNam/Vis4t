from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Teacher)
admin.site.register(University_class)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Subject_student)
admin.site.register(Subject_class)