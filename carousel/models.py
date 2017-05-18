from __future__ import unicode_literals

from django.db import models
from time import time
from django.conf import settings

def get_carousel_thumbnail_upload_path(instance, filename):
	return settings.UPLOAD_FILE_PATTERN_PREFIX + "uploaded/carousel_thumbnail/%s_%s" % (str(time()).replace('.', '_'), filename)

class Carousel(models.Model):
	thumbnail = models.ImageField(upload_to=get_carousel_thumbnail_upload_path)
	header = models.CharField(max_length=255)
	body = models.TextField()

	def __str__(self):
		return self.header

	def get_thumbnail(self):
		thumb = str(self.thumbnail)
		if not settings.DEBUG:
			thumb = thumb.replace('assets/', '')

		return thumb

class ActiveCarousel(models.Model):
	thumbnail = models.ImageField(upload_to=get_carousel_thumbnail_upload_path)
	header = models.CharField(max_length=255)
	body = models.TextField()

	def __str__(self):
		return self.header

	def get_thumbnail(self):
		thumb = str(self.thumbnail)
		if not settings.DEBUG:
			thumb = thumb.replace('assets/', '')

		return thumb