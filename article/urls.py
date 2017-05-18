from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^departments/$', views.departments),
	url(r'^departments/(?P<dept_id>\d+)/$', views.articles),
	url(r'^departments/(?P<dept_id>\d+)/(?P<article_id>\d+)/$', views.article),
	url(r'^departments/(?P<dept_id>\d+)/create/$', views.create),
	url(r'^departments/(?P<dept_id>\d+)/(?P<article_id>\d+)/like/$', views.like_article),
	url(r'^departments/(?P<dept_id>\d+)/(?P<article_id>\d+)/comment/$', views.comment),
	url(r'^departments/(?P<dept_id>\d+)/(?P<article_id>\d+)/(?P<comment_id>\d+)/deleteComment/$', views.deleteComment),
]
