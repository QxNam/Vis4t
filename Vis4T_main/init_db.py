from Vis4T_main.wsgi import *
from HomePage.models import *
from django.contrib.auth.models import User
import json
from django.contrib.auth.hashers import make_password
import pandas as pd
superuser = Teacher.objects.create_user(username='admin', password='admin', is_superuser=True, is_staff=True)
superuser.save()

t1 = Teacher(
    username='test',
    password=make_password('test'),
    first_name = 'Trương',
    last_name = 'Vĩnh Linh',
    teacher_id = "111",
    year_of_birth = 1979,
    academic_title = 'Thạc sĩ',
    major = 'Khoa học máy tính',
    sex = 'M',
    phone_number = "123456789",
    is_staff = False,
    is_active = True,
)
t1.save()

t2 = Teacher(
    username='test2',
    password=make_password('test2'),
    first_name = 'Nguyễn',
    last_name = 'Hữu Tình',
    teacher_id = "222",
    year_of_birth = 1970,
    academic_title = 'Thạc sĩ',
    major = 'Công nghệ thông tin',
    sex = 'M',
    phone_number = "234567891",
    is_staff = False,
    is_active = True,
)
t2.save()

khdl16a = University_class(
    class_name = 'KHDL16A',
    teacher = t1,
    number_of_student = 60,
    class_major = 'Khoa học dữ liệu',
    total_semester = 9,
    total_credit = 156
)
khdl16a.save()

khdl15a = University_class(
    class_name = 'KHDL15A',
    teacher = t2,
    number_of_student = 40,
    class_major = 'Khoa học máy tính', 
    total_semester = 8,
    total_credit = 146
)
khdl15a.save()

khmt13a = University_class(
    class_name = 'KHMT13A',
    teacher = t2,
    number_of_student = 40,
    class_major = 'Khoa học máy tính',
    total_semester = 8,
    total_credit = 148
)
khmt13a.save()

khmt14a = University_class(
    class_name = 'KHMT14A',
    teacher = t1,
    number_of_student = 72,
    class_major = 'Khoa học máy tính',
    total_semester = 8,
    total_credit = 128,
    is_active = False
)
khmt14a.save()

with open('../data_processing/dummy_data/KHMT14A.json', 'r', encoding='utf-8') as f:
    student_data = json.load(f)
    for i in student_data:
        s = Student(
            student_id = i['student_id'],
            class_name = khmt14a,
            student_name = i['student_name'],
            student_gmail = i['student_gmail'],
            passed_credit = i['passed_credit'],
            score_10 = i['score_10'],
            score_4 = i['score_4'],
            score_char = i['score_char'],
            rank = i['rank']
        )
        s.save()

with open('../data_processing/dummy_data/KHDL16A.json', 'r', encoding='utf-8') as f:
    student_data = json.load(f)
    for i in student_data:
        s = Student(
            student_id = i['student_id'],
            class_name = khdl16a,
            student_name = i['student_name'],
            student_gmail = i['student_gmail'],
            passed_credit = i['passed_credit'],
            score_10 = i['score_10'],
            score_4 = i['score_4'],
            score_char = i['score_char'],
            rank = i['rank']
        )
        s.save()

with open('../data_processing/dummy_data/KHMT13A.json', 'r', encoding='utf-8') as f:
    student_data = json.load(f)
    for i in student_data:
        s = Student(
            student_id = i['student_id'],
            class_name = khmt13a,
            student_name = i['student_name'],
            student_gmail = i['student_gmail'],
            passed_credit = i['passed_credit'],
            score_10 = i['score_10'],
            score_4 = i['score_4'],
            score_char = i['score_char'],
            rank = i['rank']
        )
        s.save()



with open('../data_processing/dummy_data/KHDL15A.json', 'r', encoding='utf-8') as f:
    student_data = json.load(f)
    for i in student_data:
        s = Student(
            student_id = i['student_id'],
            class_name = khdl15a,
            student_name = i['student_name'],
            student_gmail = i['student_gmail'],
            passed_credit = i['passed_credit'],
            score_10 = i['score_10'],
            score_4 = i['score_4'],
            score_char = i['score_char'],
            rank = i['rank']
        )
        s.save()
        
with open("../data_processing/dummy_data/subjects.json", 'r', encoding='utf-8') as f:
    subjects_data = json.load(f)
subjects = []
for k in subjects_data:
    r = Subject(
        subject_id = k['name_code'],
        subject_name = k['name'],
        credit = k['credit'],
    )
    subjects.append(r)
    r.save()
    
with open("../data_processing/dummy_data/subjects_class.json", 'r', encoding='utf-8') as f:
    subject_class_data = json.load(f)
for k in subject_class_data:
    class_ = University_class.objects.get(class_name=k)
    for i in subject_class_data[k]:
        Subject_class(class_name = class_, 
                      subject_id = Subject.objects.get(subject_id=i['name_code']),
                      semester_id = i['semester_id']
        ).save()
with open("../data_processing/dummy_data/KHDL15A_score.json", encoding='utf-8') as f:
    data = json.load(f)
    for i in data:
        s = Student.objects.get(student_id=i)
        for j in data[i][:2]:
            subject = Subject.objects.get(subject_name=j['subject_name'].strip())
            s.subjects.add(subject)
            Subject_student(student_id=s, subject_id=subject, score_10=j['score_10']).save()
with open("../data_processing/dummy_data/KHDL16A_score.json", encoding='utf-8') as f:
    data = json.load(f)
    for i in data:
        s = Student.objects.get(student_id=i)
        for j in data[i][:2]:
            subject = Subject.objects.get(subject_name=j['subject_name'].strip())
            s.subjects.add(subject)
            Subject_student(student_id=s, subject_id=subject, score_10=j['score_10']).save()
with open("../data_processing/dummy_data/KHMT13A_score.json", encoding='utf-8') as f:
    data = json.load(f)
    for i in data:
        s = Student.objects.get(student_id=i)
        for j in data[i][:2]:
            subject = Subject.objects.get(subject_name=j['subject_name'].strip())
            s.subjects.add(subject)
            Subject_student(student_id=s, subject_id=subject, score_10=j['score_10']).save()