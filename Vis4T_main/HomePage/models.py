from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, teacher_id, password, **extra_fields):
        if not teacher_id:
            raise ValueError('Users require an teacher_id field')
        # teacher_id = self.normalize_email(teacher_id)
        user = self.model(teacher_id=teacher_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, teacher_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(teacher_id, password, **extra_fields)

    def create_superuser(self, teacher_id, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(teacher_id, password, **extra_fields)

class Teacher(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    teacher_fullname = models.CharField(max_length=50)
    teacher_id = models.CharField(max_length = 8, unique=True)
    year_of_birth = models.IntegerField(null=True)
    academic_title = models.CharField(max_length=50)
    major = models.CharField(max_length=70)
    sex = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=10, unique=True)
    
    objects = UserManager()
    USERNAME_FIELD = 'teacher_id'
    REQUIRED_FIELDS = []

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return "{} - {}".format(self.teacher_id, self.teacher_fullname)
class University_class(models.Model):
    class_name = models.CharField(max_length=10, primary_key=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    number_of_student = models.IntegerField()
    class_major = models.CharField(max_length=70)
    teacher_note = models.TextField(blank=True)
    
    total_credit = models.IntegerField()
    is_active = models.BooleanField(default=True)
    total_semester = models.IntegerField()
    
    subjects = models.ManyToManyField('Subject', through='Subject_class')
    def __str__(self):
        return self.class_name
    


class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=8)
    class_name = models.ForeignKey('University_class', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50)
    student_gmail = models.CharField(max_length=50)
    passed_credit = models.IntegerField()
    score_10 = models.FloatField()
    score_4 = models.FloatField()
    score_char = models.CharField(max_length=2)
    rank = models.CharField(max_length=10) # học lực
    is_graduated = models.BooleanField(default=False)
    
    subjects = models.ManyToManyField('Subject', through='Subject_student', through_fields=('student', 'subject'))
    
    def __str__(self):
        return "{} - {} - {}".format(self.student_id, self.student_name, self.class_name)

class Subject_class(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    class_name = models.ForeignKey('University_class', on_delete=models.CASCADE)    
    semester_id = models.CharField(max_length=1)
    def __str__(self):
        return "{} - {} - {}".format(self.subject_id, self.class_name, self.semester_id)
                    
class Subject_student(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    score_10 = models.FloatField(null = True)
    
class Subject(models.Model):
    subject_id = models.CharField(max_length=10, primary_key=True, unique=True)
    subject_name = models.CharField(max_length=100)
    credit = models.IntegerField()
    def __str__(self):
        return "{} - {}".format(self.subject_id, self.subject_name)

class Note_student(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    content = models.TextField()
    name = models.DateTimeField(max_length=50)

class Note_class(models.Model):
    class_name = models.ForeignKey('University_class', on_delete=models.CASCADE)
    content = models.TextField()
    name = models.DateTimeField(max_length=50)