from django.conf.urls import url
from school import views

app_name = 'school'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^teacher_login/$', views.teacher_login, name="teacher_login"),
    url(r'^student_login/$', views.student_login, name="student_login"),
    url(r'^parent_login/$', views.parent_login, name="parent_login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^info/$', views.info, name="info"),
    url(r'^marks/$', views.marks, name="marks"),
    url(r'^subject_info/$', views.subject_info, name="subject_info"),
    url(r'^add_attendance/$', views.add_attendance, name="add_attendance"),
    url(r'^today_attendance/$', views.today_attendance, name="today_attendance"),
    url(r'^view_attendance/$', views.view_attendance, name="view_attendance"),
    url(r'^day_attendance/(?P<attendance_date>.*)/$', views.day_attendance, name="day_attendance"),

]