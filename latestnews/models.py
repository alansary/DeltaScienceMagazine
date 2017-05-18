from __future__ import unicode_literals

from django.db import models
from time import time
from django.conf import settings

def get_latestnews_thumbnail_upload_path(instance, filename):
	return settings.UPLOAD_FILE_PATTERN_PREFIX + 'uploaded/latestnews_thumbnail/%s_%s' % (str(time()).replace('.', '_'), filename)

# Create your models here.
class New(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	thumbnail = models.ImageField(upload_to=get_latestnews_thumbnail_upload_path)
	pub_date = models.DateTimeField()

	def __str__(self):
		return self.title

	def get_thumbnail(self):
		thumb = str(self.thumbnail)
		if not settings.DEBUG:
			thumb = thumb.replace('assets/', '')

		return thumb
