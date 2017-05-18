from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from time import time
from django.conf import settings

def get_profile_thumbnail_upload_path(instance, filename):
	return settings.UPLOAD_FILE_PATTERN_PREFIX + 'uploaded/profile_thumbnail/%s_%s' % (str(time()).replace('.', '_'), filename)

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to=get_profile_thumbnail_upload_path, default='uploaded/profile_thumbnail/default.gif')
    phone_number = models.CharField(max_length=15)
    about = models.TextField()

    def __str__(self):
    	return self.first_name + ' ' + self.last_name

    def get_image(self):
        img = str(self.profile_image)
        if not settings.DEBUG:
            img = img.replace('assets/', '')
        return img

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])