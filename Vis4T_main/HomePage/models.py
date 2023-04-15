from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class University_class(models.Model):
    class_name = models.CharField(max_length=10, primary_key=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    number_of_student = models.IntegerField()
    class_major = models.CharField(max_length=70)
    teacher_note = models.TextField(blank=True)
    def __str__(self):
        return self.class_name
    
class Teacher(AbstractUser):
    teacher_id = models.CharField(max_length = 8, unique=True)
    
    year_of_birth = models.IntegerField(null=True)
    academic_title = models.CharField(max_length=50)
    major = models.CharField(max_length=70)
    
    sex = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=10)
    
    def __str__(self):
        return "{} - {}".format(self.teacher_id, self.get_full_name())


class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=8)
    class_name = models.ForeignKey('University_class', on_delete=models.CASCADE)
    
    student_name = models.CharField(max_length=50)
    student_gmail = models.CharField(max_length=50)
    passed_credit = models.IntegerField()
    score_10 = models.FloatField()
    score_4 = models.FloatField()
    score_char = models.CharField(max_length=2)
    rank = models.CharField(max_length=10)
    
    def __str__(self):
        return "{} - {} - {}".format(self.student_id, self.student_name, self.class_name)