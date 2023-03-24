from Vis4T_main.wsgi import *
from HomePage.models import University_class, Teacher, Student
from django.contrib.auth.models import User
import json
# user = User.objects.create_user(
#     username='test',
#     password='test',
# )
superuser = User.objects.create_user(username='admin', password='admin', is_superuser=True, is_staff=True)
superuser.save()
teacher_user = User.objects.create_user(username='test', password='test')

t = Teacher(
    username='test',
    password='test',
    fullname = 'Trương Vĩnh Linh',
    teacher_id = "111",
    year_of_birth = 1979,
    academic_title = 'Thạc sĩ',
    major = 'Khoa học máy tính',
    sex = 'M',
    phone_number = "123456789",
)
t.save()

khdl16a = University_class(
    class_name = 'KHDL16A',
    teacher = t,
    number_of_student = 60,
    class_major = 'Khoa học dữ liệu'
)
khdl16a.save()

khmt16a = University_class(
    class_name = 'KHMT16A',
    teacher = t,
    number_of_student = 40,
    class_major = 'Khoa học máy tính'
)
khmt16a.save()

khmt13a = University_class(
    class_name = 'KHMT13A',
    teacher = t,
    number_of_student = 40,
    class_major = 'Khoa học máy tính'
)
khmt13a.save()


with open('final_score_KHMT13A.json', 'r', encoding='utf-8') as f:
    student_data = json.load(f)
    for i in student_data:
        Student(
            student_id = i['student_id'],
            class_name = khmt13a,
            student_name = i['student_name'],
            student_gmail = i['student_gmail'],
            passed_credit = i['passed_credit'],
            score_10 = i['score_10'],
            score_4 = i['score_4'],
            score_char = i['score_char'],
            rank = i['rank']
        ).save()