from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index1,name='index1'),
    url(r'^msg1',views.mainStuGraph1,name='testGraph1'),
]