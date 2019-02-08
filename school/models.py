from django.db import models
from datetime import *
from django.utils import timezone
# Create your models here.

class Course(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True)
    course_name = models.CharField(max_length = 200, unique=True)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    roll_no = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=200)
    student_email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 200)
    gender = models.CharField(max_length=1)
    parent_name = models.CharField(max_length=201)
    address = models.TextField(max_length=400)
    phone_no = models.CharField(max_length = 10, unique=True)
    department = models.CharField(max_length=30)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20, primary_key=True)
    teacher_name = models.CharField(max_length=200)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 200)
    phone_no = models.CharField(max_length = 10, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.teacher_name


class Attendance(models.Model):
    student = models.CharField(max_length = 200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=0) 
    teacher = models.CharField(max_length = 200)
    attendance_date = models.DateField('date published', default=date.today)
    update_date = models.DateTimeField('date published', default=timezone.now)


class Subject(models.Model):
    subject_id = models.CharField(max_length=20, primary_key=True)
    subject_name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.subject_name

class Exam(models.Model):
    exam_id = models.CharField(max_length=20)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)
    marks = models.IntegerField(default=10)

