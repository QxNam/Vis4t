# Generated by Django 4.1.7 on 2023-11-16 18:36

import HomePage.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=50)),
                ('student_gmail', models.CharField(max_length=50)),
                ('passed_credit', models.IntegerField()),
                ('score_10', models.FloatField()),
                ('score_4', models.FloatField()),
                ('score_char', models.CharField(max_length=3)),
                ('rank', models.CharField(max_length=20)),
                ('is_graduated', models.BooleanField(default=False)),
                ('lastname', models.CharField(max_length=15, null=True)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('subject_name', models.CharField(max_length=100)),
                ('credit', models.IntegerField()),
            ],
            options={
                'db_table': 'Subject',
            },
        ),
        migrations.CreateModel(
            name='Subject_class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_id', models.CharField(max_length=1, null=True)),
                ('is_mandatory', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Subject_class',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('teacher_fullname', models.CharField(max_length=50)),
                ('teacher_id', models.CharField(max_length=8, unique=True)),
                ('year_of_birth', models.IntegerField(null=True)),
                ('academic_title', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=70)),
                ('sex', models.CharField(max_length=3)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'Teacher',
            },
            managers=[
                ('objects', HomePage.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='University_class',
            fields=[
                ('class_name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('number_of_student', models.IntegerField(null=True)),
                ('class_major', models.CharField(max_length=70)),
                ('total_credit', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('total_semester', models.IntegerField()),
                ('subjects', models.ManyToManyField(through='HomePage.Subject_class', to='HomePage.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'University_class',
            },
        ),
        migrations.CreateModel(
            name='Typesense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node', models.CharField(max_length=100, null=True, unique=True)),
                ('admin_key', models.CharField(max_length=100, null=True, unique=True)),
                ('search_key', models.CharField(max_length=100, null=True, unique=True)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.university_class')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'TypesenseApi',
            },
        ),
        migrations.CreateModel(
            name='Subject_student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_10', models.FloatField(null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.student')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomePage.subject')),
            ],
            options={
                'db_table': 'Subject_student',
            },
        ),
        migrations.AddField(
            model_name='subject_class',
            name='class_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.university_class'),
        ),
        migrations.AddField(
            model_name='subject_class',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.subject'),
        ),
        migrations.AddField(
            model_name='student',
            name='class_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.university_class'),
        ),
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(through='HomePage.Subject_student', to='HomePage.subject'),
        ),
        migrations.CreateModel(
            name='Note_student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('name', models.DateField(max_length=50)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.student')),
            ],
            options={
                'db_table': 'Note_student',
            },
        ),
        migrations.CreateModel(
            name='Note_class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('name', models.DateField(max_length=50)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.university_class')),
            ],
            options={
                'db_table': 'Note_class',
            },
        ),
    ]
