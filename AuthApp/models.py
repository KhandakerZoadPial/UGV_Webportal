from distutils.command.upload import upload
from operator import mod
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    student_id = models.TextField(blank=True)
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    date_of_birth = models.TextField(blank=True)
    gender = models.TextField(blank=True)
    address = models.TextField(blank=True)
    contact_number = models.TextField(blank=True)
    hsc_background = models.TextField(blank=True)
    HSC_Registration_Number = models.TextField(blank=True)
    hsc_passing_year = models.TextField(blank=True)
    Program = models.TextField(blank=True)
    local_guardian_name = models.TextField(blank=True)
    local_guardian_relation = models.TextField(blank=True)
    local_guardian_contact_number = models.TextField(blank=True)
    local_guardian_address = models.TextField(blank=True)
    semester = models.IntegerField(default=1)

    marksheet = models.FileField(upload_to='marksheets')
    student_photo = models.ImageField(upload_to='student_photos')

    def __str__(self):
        return self.student_id


class id_tracker(models.Model):
    position = models.IntegerField()


DEPT_CHOICES = (
    ("CSE", "CSE"),
    ("BBA", "BBA"),
    ("CE", "CE"),
    ("ME", "ME"),
    ("EEE", "EEE"),
)

class TeacherProfile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher_name = models.TextField()
    gender = models.TextField(blank=True)
    photo = models.ImageField(upload_to='student_photos')
    dept = models.CharField(max_length=9, choices=DEPT_CHOICES)
    teacher_code = models.CharField(max_length=10)
    teacher_id = models.TextField(blank=True)


class Coursees(models.Model):
    course_name = models.TextField()
    course_code = models.TextField()
    course_teacher = models.ForeignKey(TeacherProfile, on_delete=models.DO_NOTHING)
    course_semester = models.IntegerField(default=0)


class Notes(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    date = models.DateField(auto_now_add=True)