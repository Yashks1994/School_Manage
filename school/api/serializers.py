from rest_framework.serializers import ModelSerializer

from school.models import *

class PostSerializers(ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'roll_no',
            'name',
            'student_email',
            'gender',
            'parent_name',
            'address',
            'phone_no',
            'department',
            'course',
        ]
