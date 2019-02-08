from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView,
    #UpdateAPIView,
    #DestroyAPIView
)
from school.models import *
from .serializers import PostSerializers

class PostListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = PostSerializers

class PostDetailAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = PostSerializers

#class PostUpdateAPIView(UpdateAPIView):
#    queryset = Student.objects.all()
#    serializer_class = PostSerializers

#class PostDeleteAPIView(DestroyAPIView):
#    queryset = Student.objects.all()
#    serializer_class = PostSerializers



