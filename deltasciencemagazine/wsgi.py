"""
WSGI config for deltasciencemagazine project.
=======
WSGI config for deltascienceproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

# default
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deltasciencemagazine.settings")

# whitenoise
application = get_wsgi_application()
application = DjangoWhiteNoise(application)

try:
	from dj_static import Cling
	application = Cling(get_wsgi_application())
except:
	pass