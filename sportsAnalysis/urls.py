from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^myticket/$', views),
    url(r'^sg1p0',views.sportsAnalysisGraph1),
    url(r'^sg2p0',views.sportsAnalysisGraphChronological),
    url(r'^sg3p0',views.sportsRadarAnalysis),
]