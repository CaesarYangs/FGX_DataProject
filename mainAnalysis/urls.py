from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index1,name='index1'),
    url(r'^msg1p0',views.mainStuGraph1),
    url(r'^msg1p1',views.mainStuGraph1_1),
    url(r'^msg1p2',views.mainStuGraph1_2),
]