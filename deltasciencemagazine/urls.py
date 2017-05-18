"""deltasciencemagazine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from contact import views as contact_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_page),
    url(r'^department/', include('article.urls')),
    url(r'^accounts/login/$', views.login_view),
    url(r'^accounts/auth/$', views.auth_view),
    url(r'^accounts/success_login/$', views.success_login),
    url(r'^accounts/invalid_login/$', views.invalid_login),
    url(r'^accounts/register_user/$', views.register_user),
    url(r'^accounts/successful_register/$', views.successful_register),
    url(r'^accounts/logout/$', views.logout_user),
    url(r'^contact/', include('contact.urls')),
    url(r'^latestnews/', include('latestnews.urls')),
    url(r'^developer/', include('developer.urls')),
    url(r'^profile/', include('userprofile.urls')),
    url(r'^notification/', include('notification.urls')),
    url(r'^volumes/', include('volume.urls')),
]

admin.site.site_title = ('Alansary')
admin.site.site_header = ('Control Panel')
admin.site.index_header = ('Administration')

from django.conf import settings
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)