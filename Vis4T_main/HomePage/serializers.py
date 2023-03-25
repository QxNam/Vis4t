from rest_framework import serializers

from .models import *

class University_classSerializer(serializers.ModelSerializer):
    class Meta:
        model = University_class
        fields = '__all__'
    
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['teacher_id', 'fullname', 'year_of_birth', 'academic_title', 'major', 'sex', 'phone_number']
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'