from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Notification(models.Model):
	title = models.CharField(max_length=255)
	message = models.TextField()
	viewed = models.BooleanField(default=False)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.title

@receiver(post_save, sender=User)
def create_welcome_message(sender, **kwargs):
	if kwargs.get('created', False):
		Notification.objects.create(user=kwargs.get('instance'),
			title="Welcome to our Magazine!",
			message="Thanks for signing up, you can edit your profile and create new articles!")