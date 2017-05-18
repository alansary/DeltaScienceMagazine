from __future__ import unicode_literals

from django.db import models
from time import time
from django.contrib.auth.models import User
from django.conf import settings

def get_article_thumbnail_upload_path(instance, filename):
	return settings.UPLOAD_FILE_PATTERN_PREFIX + 'uploaded/article_thumbnail/%s_%s' % (str(time()).replace('.', '_'), filename)

def get_department_thumbnail_upload_path(instance, filename):
	return settings.UPLOAD_FILE_PATTERN_PREFIX + 'uploaded/department_thumbnail/%s_%s' % (str(time()).replace('.', '_'), filename)

# Create your models here.
class Department(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	thumbnail = models.FileField(upload_to=get_department_thumbnail_upload_path)

	def __str__(self):
		return self.title

	def get_thumbnail(self):
		thumb = str(self.thumbnail)
		if not settings.DEBUG:
			thumb = thumb.replace('assets/', '')

		return thumb

class Article(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	pub_date = models.DateTimeField('publication date')
	likes = models.IntegerField(default=0)
	thumbnail = models.ImageField(upload_to=get_article_thumbnail_upload_path, default=settings.UPLOAD_FILE_PATTERN_PREFIX + 'uploaded/article_thumbnail/default.jpg')
	department = models.ForeignKey(Department)
	username = models.CharField(max_length=255)
	approved = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def get_thumbnail(self):
		thumb = str(self.thumbnail)
		if not settings.DEBUG:
			thumb = thumb.replace('assets/', '')

		return thumb

class Comment(models.Model):
	name = models.CharField(max_length=255)
	comment = models.TextField()
	pub_date = models.DateTimeField('date published')
	article = models.ForeignKey(Article)
	username = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class ArticleLikes(models.Model):
	article_id = models.IntegerField()
	user_id = models.IntegerField()

	def __str__(self):
		return str(self.article_id) + ' ' + str(self.user_id)

class MostPopular(models.Model):
	article = models.ForeignKey(Article)