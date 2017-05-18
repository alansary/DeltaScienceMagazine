from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'volumes/$', views.volumes),
	url(r'volumes/(?P<year_id>\d+)/(?P<volume_id>\d+)/$', views.volume),
	url(r'volumes/(?P<year_id>\d+)/(?P<volume_id>\d+)/(?P<paper_id>\d+)/$', views.paper),
]