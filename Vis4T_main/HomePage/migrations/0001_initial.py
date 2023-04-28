
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


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
                ('score_char', models.CharField(max_length=2)),
                ('rank', models.CharField(max_length=10)),
                ('is_graduated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('subject_name', models.CharField(max_length=100)),
                ('credit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject_class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_id', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('teacher_id', models.CharField(max_length=8, unique=True)),
                ('year_of_birth', models.IntegerField(null=True)),
                ('academic_title', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=70)),
                ('sex', models.CharField(max_length=3)),
                ('phone_number', models.CharField(max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='University_class',
            fields=[
                ('class_name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('number_of_student', models.IntegerField()),
                ('class_major', models.CharField(max_length=70)),
                ('teacher_note', models.TextField(blank=True)),
                ('total_credit', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('total_semester', models.IntegerField()),
                ('subjects', models.ManyToManyField(through='HomePage.Subject_class', to='HomePage.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject_student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_10', models.FloatField(null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.student')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomePage.subject')),
            ],
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
    ]
