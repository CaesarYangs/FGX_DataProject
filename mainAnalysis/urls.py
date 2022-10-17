from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index1,name='index1'),
    url(r'^msg1p0',views.mainStuGraph1),
    url(r'^msg1p1',views.mainStuGraph1_1),
    url(r'^msg1p2',views.mainStuGraph1_2),
    url(r'^msg2',views.mainStuGraph2),
    url(r'^msg3p0',views.mainStuGraph3),
    url(r'^msg3p1',views.mainStuGraph3_1),
    url(r'^msg3p2',views.mainStuGraph3_1),
    url(r'^ga1p0',views.mainGradeAnalysis1),
]