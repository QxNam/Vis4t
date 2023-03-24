from django.db import models

# Create your models here.
class University_class(models.Model):
    class_name = models.CharField(max_length=10, primary_key=True, unique=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    number_of_student = models.IntegerField()
    class_major = models.CharField(max_length=70)
    def __str__(self):
        return self.class_name
    
class Teacher(models.Model):
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    
    teacher_id = models.BigAutoField(primary_key=True, unique=True)
    fullname = models.CharField(max_length=50)
    year_of_birth = models.IntegerField()
    academic_title = models.CharField(max_length=50)
    major = models.CharField(max_length=70)
    
    sex = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=10)
    
    def __str__(self):
        res = """fullname: {}\n
        login_name: {}\n
        password: {}\n
        """.format(self.fullname, self.login_name, self.password)
        return res

