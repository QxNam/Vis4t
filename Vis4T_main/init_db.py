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
    class_major = 'Khoa Học Dữ Liệu',
    total_semester = 9,
    total_credit = 156
)
khdl16a.save()

khdl15a = University_class(
    class_name = 'KHDL15A',
    teacher = t2,
    number_of_student = 40,
    class_major = 'Khoa Học Dữ Liệu', 
    total_semester = 8,
    total_credit = 146
)
khdl15a.save()

khmt13a = University_class(
    class_name = 'KHMT13A',
    teacher = t2,
    number_of_student = 40,
    class_major = 'Khoa Học Máy Tính',
    total_semester = 8,
    total_credit = 148
)
khmt13a.save()

khmt14a = University_class(
    class_name = 'KHMT14A',
    teacher = t1,
    number_of_student = 72,
    class_major = 'Khoa Học Máy Tính',
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
        subject_name = k['name'].strip(),
        credit = k['credit'],
    )
    subjects.append(r)
    r.save()
    
with open("../data_processing/dummy_data/subjects_class.json", 'r', encoding='utf-8') as f:
    subject_class_data = json.load(f)
for k in subject_class_data:
    class_ = University_class.objects.get(class_name=k)
    for i in subject_class_data[k]:
        subject = Subject.objects.get(subject_id=i['name_code'])
        Subject_class.objects.create(
            class_name = class_, 
            subject = Subject.objects.get(subject_id=i['name_code']),
            semester_id = i['semester_id']
        )
        
class_name = ['KHMT13A', 'KHDL16A', 'KHDL15A']
for i in class_name:
    uc = University_class.objects.get(class_name=i)
    with open(f"../data_processing/dummy_data/{i}_score.json", encoding='utf-8') as f:
        data = json.load(f)
        for i in data:
            s = Student.objects.get(student_id=i)
            for j in data[i]:
                if j['score_10'] < 0:
                    continue
                subject_class = Subject_class.objects.filter(class_name=uc, subject__subject_name=j['subject_name'].strip()).first()
                if subject_class is None:
                    try:
                        subject = Subject.objects.filter(subject_name__icontains=j['subject_name'].strip()).first()
                    except:
                        print(uc, j)
                        continue
                else:
                    subject = subject_class.subject          
                subject_student = Subject_student(
                    student = s,
                    subject = subject,
                    score_10 = float(j['score_10'])
                )
                subject_student.save()
                s.subjects.add(subject)
 