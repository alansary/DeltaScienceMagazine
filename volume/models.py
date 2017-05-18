from __future__ import unicode_literals
from django.db import models
from time import time
from django.contrib.auth.models import User
from django.conf import settings

def get_paper_file_upload_path(instance, filename):
	return settings.UPLOAD_FILE_PATTERN_PREFIX + 'uploaded/paper_file/%s_%s' % (str(time()).replace('.', '_'), filename)

# Create your models here.
class Year(models.Model):
	startDate = models.DateTimeField()
	endDate = models.DateTimeField()

	def __str__(self):
		return str(self.startDate) + ' - ' + str(self.endDate)

class Volume(models.Model):
	year = models.ForeignKey(Year)
	title = models.CharField(max_length=255)
	number = models.IntegerField()
	date = models.DateTimeField()

	def __str__(self):
		return self.title + ' ' + str(self.number)

class Paper(models.Model):
	volume = models.ForeignKey(Volume)
	abstract = models.TextField()
	keywords = models.TextField()
	file = models.FileField(upload_to=get_paper_file_upload_path)
	number = models.IntegerField()
	date = models.DateTimeField()
	title = models.CharField(max_length=255)
	user = models.ManyToManyField(User)

	def __str__(self):
		return self.title + ' ' + str(self.number)

	def get_file(self):
		f = str(self.file)
		if not settings.DEBUG:
			f = f.replace('assets/', '')

		return f

class Highlight(models.Model):
	paper = models.ForeignKey(Paper)
	highlight = models.TextField()
	number = models.IntegerField()

	def __str__(self):
		return self.highlight

class Author(models.Model):
	paper = models.ForeignKey(Paper)
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class MostPopularPaper(models.Model):
	paper = models.ForeignKey(Paper)

	def __str__(self):
		return self.paper.title
