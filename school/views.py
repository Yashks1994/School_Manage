from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.contrib import messages
from django.views import generic
from datetime import *
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm

# Create your views here.

def index(request):

    my_dict = {'insert_me': 'Hello I am New'}

    return render(request, 'school/home.html', context=my_dict)


def teacher_login(request):
    if request.method == 'POST':
        try:
            teacher_data = Teacher.objects.get(email = request.POST['email'])
            if teacher_data:
                if teacher_data.password == request.POST['password']:  
                    request.session['teacher'] = teacher_data.teacher_id
                    
                    return HttpResponseRedirect(reverse('school:dashboard'))
                    
                else:
                    content = {
                    'data': teacher_data
                    }
                    messages.error(request, 'Sorry, either of your provided information is wrong.')
                    return render(request, 'school/teacher_login.html', content)
        except ObjectDoesNotExist:
            return render(request, 'school/home.html')
    else:
        return render(request, 'school/teacher_login.html')

def student_login(request):
    if request.method == 'POST':
        try:
            student_data = Student.objects.get(student_email = request.POST['student_email'])
            if student_data:
                if student_data.password == request.POST['password']:  
                    request.session['student'] = student_data.roll_no
                    
                    response = HttpResponseRedirect(reverse('school:dashboard'))
                    return response
                else:
                    content = {
                    'data': student_data
                    }
                    messages.error(request, 'Sorry, either of your provided information is wrong.')
                    return render(request, 'school/student_login.html', content)
        except ObjectDoesNotExist:
            return render(request, 'school/home.html')
    else:
        return render(request, 'school/student_login.html')

def parent_login(request):
    if request.method == 'POST':
        try:
            parent_data = Student.objects.get(roll_no = request.POST['roll_no'])
            if parent_data:
                if parent_data.name == request.POST['name']:  
                    request.session['parent'] = parent_data.roll_no
                    
                    response = HttpResponseRedirect(reverse('school:dashboard'))
                    return response
                else:
                    content = {
                    'data': parent_data
                    }
                    messages.error(request, 'Sorry, either of your provided information is wrong.')
                    return render(request, 'school/parent_login.html', content)
        except ObjectDoesNotExist:
            return render(request, 'school/home.html')
    else:
        return render(request, 'school/parent_login.html')



def dashboard(request):
    if 'teacher' in request.session:
        sessn_val = request.session['teacher']
        return render(request, 'school/dashboard.html')
    elif 'student' in request.session:
        sessn_val = request.session['student']
        return render(request, 'school/dashboard.html')
    elif 'parent' in request.session:
        sessn_val = request.session['parent']
        student_data = Student.objects.all().filter(roll_no=sessn_val)
        for i in student_data:
            j = i.course
        teacher_data = Teacher.objects.all().filter(course= j)
        subject_data = Subject.objects.all().filter(course= j)
        course_data = Course.objects.all().filter(course_name=j)
        context = {'student_data': student_data, 'teacher_data': teacher_data, 'subject_data':subject_data, 'course_data':course_data}
        return render(request, 'school/dashboard.html', context)


def logout(request):
    try:
        if 'teacher' in request.session:
            del request.session['teacher']
        elif 'student' in request.session:
            del request.session['student']
        elif 'parent' in request.session:
            del request.session['parent']
    except KeyError:
        pass

    #messages.success(request, "Logged Out Successfully")
    return HttpResponseRedirect(reverse('school:index'))

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'school/signup.html', {'form': form})
    
# Viewing the Student or Teacher Info

def info(request):
    if 'teacher' in request.session:
        sessn_val = request.session['teacher']
        teacher_data = Teacher.objects.all().filter(teacher_id=sessn_val)
        for i in teacher_data:
            j = i.course
        subject_data = Subject.objects.all().filter(course= j)
        course_data = Course.objects.all().filter(course_name=j)
        content = {'teacher_data': teacher_data, 'subject_data':subject_data, 'course_data':course_data}
        return render(request, 'school/personal_info.html', content)
    elif 'student' in request.session:
        sessn_val = request.session['student']
        student_data = Student.objects.all().filter(roll_no=sessn_val)
        for i in student_data:
            j = i.course
        teacher_data = Teacher.objects.all().filter(course= j)
        subject_data = Subject.objects.all().filter(course= j)
        course_data = Course.objects.all().filter(course_name=j)
        content = {'student_data': student_data, 'teacher_data': teacher_data, 'subject_data':subject_data, 'course_data':course_data}
        return render(request, 'school/personal_info.html', content)
    elif 'parent' in request.session:
        sessn_val = request.session['parent']
        student_data = Student.objects.all().filter(roll_no=sessn_val)
        for i in student_data:
            j = i.course
        teacher_data = Teacher.objects.all().filter(course= j)
        subject_data = Subject.objects.all().filter(course= j)
        course_data = Course.objects.all().filter(course_name=j)
        content = {'student_data': student_data, 'teacher_data': teacher_data, 'subject_data':subject_data, 'course_data':course_data}
        return render(request, 'school/personal_info.html', content)

def subject_info(request):
    if 'teacher' in request.session:
        sessn_val = request.session['teacher']
        teacher_data = Teacher.objects.all().filter(teacher_id=sessn_val)
        for i in teacher_data:
            j = i.course
        subject_data = Subject.objects.all().filter(course= j)
        course_data = Course.objects.all().filter(course_name=j)
        content = {'teacher_data': teacher_data, 'subject_data':subject_data, 'course_data':course_data}
        return render(request, 'school/subjects.html', content)
    elif 'student' in request.session:
        sessn_val = request.session['student']
        student_data = Student.objects.all().filter(roll_no=sessn_val)
        for i in student_data:
            j = i.course
        teacher_data = Teacher.objects.all().filter(course= j)
        subject_data = Subject.objects.all().filter(course= j)
        course_data = Course.objects.all().filter(course_name=j)
        content = {'student_data': student_data, 'teacher_data': teacher_data, 'subject_data':subject_data, 'course_data':course_data}
        return render(request, 'school/subjects.html', content)
    elif 'parent' in request.session:
        sessn_val = request.session['parent']
        student_data = Student.objects.all().filter(roll_no=sessn_val)
        for i in student_data:
            j = i.course_id
        teacher_data = Teacher.objects.all().filter(course= j)
        subject_data = Subject.objects.all().filter(course= j)
        course_data = Course.objects.all().filter(course_name=j)
        context = {'student_data': student_data, 'teacher_data': teacher_data, 'subject_data':subject_data, 'course_data':course_data}
        return render(request, 'school/subjects.html', context)

def marks(request):
    return render(request, 'school/marks.html')

# For Viewing and Adding the Attendance  

def add_attendance(request):
    sessn_val = request.session['teacher']
    teacher_data = Teacher.objects.get(pk=sessn_val)
    course_data = Course.objects.get(course_name=teacher_data.course)
    content = { 'teacher_data': teacher_data, 'course_data': course_data }
    return render(request, 'school/add_attendance.html', content)

def view_attendance(request):
    if 'teacher' in request.session:
        teacher_data = Teacher.objects.get(pk = request.session['teacher'])
        course_data = Course.objects.get(course_name=teacher_data.course)
        attendance_data = Attendance.objects.filter(course = course_data.pk)
        content = { 'teacher_data': teacher_data, 'attendance_data' : attendance_data, 'course_data': course_data }
        return render(request, 'school/view_attendance.html', content)
    elif 'student' in request.session:
        student_data = Student.objects.get(pk=request.session['student'])
        course_data = Course.objects.get(course_name=student_data.course)    
        attendance_data = Attendance.objects.filter(course = course_data.pk )
        content = { 'attendance_data' : attendance_data, 'student_data': student_data, 'course_data':course_data }
    return render(request, 'school/view_attendance_student.html', content)

def day_attendance(request, attendance_date):
    if 'teacher' in request.session:
        teacher_data = Teacher.objects.get(pk = request.session['teacher'])
        course_data = Course.objects.get(course_name=teacher_data.course)
        attendance_data = Attendance.objects.filter(teacher = teacher_data.teacher_name, attendance_date = attendance_date )
        content = {  'teacher_data': teacher_data, 'attendance_data' : attendance_data, 'course_data': course_data }
        return render(request, 'school/day_attendance.html', content)
    return render(request, 'school/day_attendance.html', content)

def today_attendance(request):
    if request.method == 'POST':
        total_students = request.POST['total_studnt']
        student = ','.join(request.POST.getlist('present[]'))
        teacher_data = Teacher.objects.get(pk = request.session['teacher'])
        course_data = Course.objects.get(course_name=teacher_data.course)
        add_attendance = course_data.attendance_set.create(student=student, course=request.POST.get('course'), teacher=request.session['teacher'])
        add_attendance.save()
        #messages.success(request, 'Attendance Added Successfully.')
    return render(request, 'school/add_attendance.html')