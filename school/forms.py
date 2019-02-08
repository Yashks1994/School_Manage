from django import forms
from .models import *


class RegistrationForm(forms.ModelForm):
    roll_no = forms.CharField(label='Roll No', max_length=20)
    name = forms.CharField(label='Name', max_length=200)
    student_email = forms.EmailField(label='Email', max_length = 100)
    password = forms.CharField(label='Password', max_length = 200)
    gender = forms.CharField(label='Gender', max_length=1, help_text='Required. M or F')
    parent_name = forms.CharField(label='Parent Name', max_length=201)
    address = forms.CharField(label='Address', max_length=1000)
    phone_no = forms.IntegerField(label='Phone Number', max_value=1000000000)
    department = forms.CharField(label='Department', max_length=200, help_text='B.E or Pharma')
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label='Course Name')

    # if we use flat then it will not create as a tupple i.e Course.objects.values_list('course_id', flat=True)
    
    class Meta:
        model = Student
        fields = ('roll_no', 'name', 'student_email', 'password', 'gender', 'parent_name', 'address', 'phone_no', 'department', 'course' )