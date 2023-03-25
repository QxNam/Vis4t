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
teacher_user1 = User.objects.create_user(username='test', password='test')
teacher_user2 = User.objects.create_user(username='test2', password='test2')


t1 = Teacher(
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
t1.save()

t2 = Teacher(
    username='test2',
    password='test2',
    fullname = 'Nguyễn Hữu Tình',
    teacher_id = "222",
    year_of_birth = 1970,
    academic_title = 'Thạc sĩ',
    major = 'Công nghệ thông tin',
    sex = 'M',
    phone_number = "234567891",
)
t2.save()
khdl16a = University_class(
    class_name = 'KHDL16A',
    teacher = t1,
    number_of_student = 60,
    class_major = 'Khoa học dữ liệu'
)
khdl16a.save()

khdl15a = University_class(
    class_name = 'KHDL15A',
    teacher = t2,
    number_of_student = 40,
    class_major = 'Khoa học máy tính'
)
khdl15a.save()

khmt13a = University_class(
    class_name = 'KHMT13A',
    teacher = t2,
    number_of_student = 40,
    class_major = 'Khoa học máy tính'
)
khmt13a.save()


with open('dummy_data/final_score_KHMT13A.json', 'r', encoding='utf-8') as f:
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
        
with open('dummy_data/final_score_KHDL15A.json', 'r', encoding='utf-8') as f:
    student_data = json.load(f)
    for i in student_data:
        Student(
            student_id = i['student_id'],
            class_name = khdl15a,
            student_name = i['student_name'],
            student_gmail = i['student_gmail'],
            passed_credit = i['passed_credit'],
            score_10 = i['score_10'],
            score_4 = i['score_4'],
            score_char = i['score_char'],
            rank = i['rank']
        ).save()