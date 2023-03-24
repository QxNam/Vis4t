from Vis4T_main.wsgi import *
from HomePage.models import University_class, Teacher
from django.contrib.auth.models import User

# user = User.objects.create_user(
#     username='test',
#     password='test',
# )

t = Teacher(
    login_name='test',
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

httt16a = University_class(
    class_name = 'HTTT16B',
    teacher = t,
    number_of_student = 80,
    class_major = 'Hệ thống thông tin'
)
httt16a.save()
