from __future__ import unicode_literals

from django.db import models
from time import time
from django.conf import settings

def get_developer_thumbnail_upload_path(instance, filename):
	return settings.UPLOAD_FILE_PATTERN_PREFIX + 'uploaded/developer_thumbnail/%s_%s' % (str(time()).replace('.', '_'), filename)

def get_certificate_thumbnail_upload_path(instance, filename):
	return settings.UPLOAD_FILE_PATTERN_PREFIX + 'uploaded/certificate_thumbnail/%s_%s' % (str(time()).replace('.', '_'), filename)

# Create your models here.
class Skill(models.Model):
	skill = models.CharField(max_length=255)
	level = models.IntegerField()

	def __str__(self):
		return self.skill

class CertificatesAndCourses(models.Model):
	fromDate = models.CharField(max_length=25)
	toDate = models.CharField(max_length=25)
	title = models.CharField(max_length=255)
	issuedBy = models.CharField(max_length=255)
	description = models.TextField()
	courseImage = models.ImageField(upload_to=get_certificate_thumbnail_upload_path)

	def __str__(self):
		return self.title

	def get_thumbnail(self):
		thumb = str(self.courseImage)
		if not settings.DEBUG:
			thumb = thumb.replace('assets/', '')

		return thumb

class Summary(models.Model):
	info = models.TextField()

	def __str__(self):
		return self.info

class PersonalDetails(models.Model):
	fullName = models.CharField(max_length=50)
	jobTitle = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	country = models.CharField(max_length=20)
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	personalImage = models.ImageField(upload_to=get_developer_thumbnail_upload_path)

	def get_thumbnail(self):
		thumb = str(self.personalImage)
		if not settings.DEBUG:
			thumb = thumb.replace('assets/', '')

		return thumb

class Languages(models.Model):
	language = models.CharField(max_length=20)
	level = models.CharField(max_length=20)
