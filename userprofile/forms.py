from django import forms
from .models import UserProfile
from django.forms import TextInput
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ('first_name', 'last_name', 'phone_number', 'about', 'profile_image')

