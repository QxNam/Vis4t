from django.db import models

# Create your models here.
class University_class(models.Model):
    class_name = models.CharField(max_length=10, primary_key=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    number_of_student = models.IntegerField()
    class_major = models.CharField(max_length=70)
    def __str__(self):
        return self.class_name
    
class Teacher(models.Model):
    username = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100)
    
    teacher_id = models.CharField(max_length = 8, unique=True)
    fullname = models.CharField(max_length=50)
    year_of_birth = models.IntegerField()
    academic_title = models.CharField(max_length=50)
    major = models.CharField(max_length=70)
    
    sex = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=10)
    
    def __str__(self):
        res = """fullname: {}\t
        login_name: {}\t
        password: {}\t
        """.format(self.fullname, self.username, self.password)
        return res


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