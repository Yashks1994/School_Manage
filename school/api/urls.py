from django.conf.urls import url
from school import views
from .views import ( 
    PostListAPIView,
    PostDetailAPIView,
    #PostUpdateAPIView,
    #PostDeleteAPIView
    )

urlpatterns = [
    url(r'^$', PostListAPIView.as_view() , name='list'),
    url(r'^(?P<pk>\d+)/$', PostDetailAPIView.as_view() , name='details'),
    #url(r'^(?P<pk>\d+)/edit$', PostUpdateAPIView.as_view() , name='update'),
    #url(r'^(?P<pk>\d+)/delete/$', PostDeleteAPIView.as_view() , name='delete'),
]