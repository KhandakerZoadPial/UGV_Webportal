# Generated by Django 4.0.3 on 2022-03-12 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AuthApp', '0003_alter_studentprofile_marksheet_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.TextField()),
                ('gender', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='student_photos')),
                ('dept', models.CharField(choices=[('CSE', 'CSE'), ('BBA', 'BBA'), ('CE', 'CE'), ('ME', 'ME'), ('EEE', 'EEE')], max_length=9)),
                ('teacher_code', models.CharField(max_length=10)),
                ('teacher_id', models.TextField(blank=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Coursees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.TextField()),
                ('course_code', models.TextField()),
                ('course_semester', models.IntegerField(default=0)),
                ('course_teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AuthApp.teacherprofile')),
            ],
        ),
    ]
