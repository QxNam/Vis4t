from rest_framework import serializers

from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'student_name', 'student_gmail', 'passed_credit', 'score_10', 'score_4', 'score_char', 
                  'rank', 'is_graduated']

class University_classSerializer(serializers.ModelSerializer):
    class Meta:
        model = University_class
        fields = '__all__'
    
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['teacher_id', 'fullname', 'year_of_birth', 'academic_title', 'major', 'sex', 'phone_number']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['subject_name', 'score_10', 'credit']
    
