# Generated by Django 4.1.7 on 2023-03-25 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('teacher_id', models.CharField(max_length=8, unique=True)),
                ('fullname', models.CharField(max_length=50)),
                ('year_of_birth', models.IntegerField()),
                ('academic_title', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=70)),
                ('sex', models.CharField(max_length=3)),
                ('phone_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='University_class',
            fields=[
                ('class_name', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('number_of_student', models.IntegerField()),
                ('class_major', models.CharField(max_length=70)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=50)),
                ('student_gmail', models.CharField(max_length=50)),
                ('passed_credit', models.IntegerField()),
                ('score_10', models.FloatField()),
                ('score_4', models.FloatField()),
                ('score_char', models.CharField(max_length=2)),
                ('rank', models.CharField(max_length=10)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.university_class')),
            ],
        ),
    ]
