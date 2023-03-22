from django.db import models

# Create your models here.

class Class(models.Model):
    class_id = models.BigAutoField(primary_key=True, unique=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    number_of_student = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    login_name = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    
    
    teacher_id = models.BigAutoField(primary_key=True, unique=True)
    fullname = models.CharField(max_length=50)
    year_of_birth = models.IntegerField()
    sex = models.CharField(max_length=3)
    start_work_year = models.IntegerField()
    academic_title = models.CharField(max_length=50)
    major = models.CharField(max_length=70)
    
    def __str__(self):
        res = """fullname: {}\n
        login_name: {}\n
        password: {}\n
        """.format(self.fullname, self.login_name, self.password)
        return res

