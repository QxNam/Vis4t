from django.db import models

# Create your models here.

class Class(models.Model):
    class_id = models.BigAutoField(primary_key=True, unique=True)
    
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    teacher_id = models.BigAutoField(primary_key=True, unique=True)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)
    login_name = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    
    
    fullname = models.CharField(max_length=50)
    def __str__(self):
        res = """fullname: {}\n
        login_name: {}\n
        password: {}\n
        """.format(self.fullname, self.login_name, self.password)
        return res

