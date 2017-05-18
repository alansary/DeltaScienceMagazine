from django.conf.urls import url
from .models import New
from . import views

urlpatterns = [
	url(r'^(?P<new_id>\d+)/$', views.new),
	url(r'^news/$', views.news),
]