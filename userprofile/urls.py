from django.conf.urls import url
from .views import userprofile, editprofile

urlpatterns = [
	url(r'(?P<user_name>[a-z\d]+)/edit/$', editprofile),
	url(r'(?P<user_name>[a-z\d]+)/$', userprofile),
]