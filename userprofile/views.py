from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from article.models import Article
from .forms import UserProfileForm
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from notification.models import Notification
from volume.models import Paper

# Create your views here.
def userprofile(request, user_name):
	if request.user.is_authenticated and user_name == request.user.username:
		validity = True
	else:
		validity = False
	context = {}
	context['validity'] = validity
	context['currentUser'] = request.user
	context['requiredUser'] = user_name
	try:
		context['articles'] = Article.objects.filter(username=user_name)
	except:
		context['articles'] = {}
	context['userinfo'] = UserProfile.objects.filter(user=User.objects.get(username=user_name))
	context['notifications'] = Notification.objects.filter(user=request.user, viewed=False)
	try:
		context['papers'] = Paper.objects.filter(user=User.objects.get(username=user_name))
	except:
		context['papers'] = {}
	return render_to_response('profile.html', context)

@login_required
def editprofile(request, user_name):
	if request.user.is_authenticated and user_name == request.user.username:
		if request.POST:
			form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
			if form.is_valid():
				temp = form.save(commit=False)
				temp.user = request.user
				temp.save()
				return HttpResponseRedirect('/profile/%s' % request.user.username)
		else:
			user = request.user
			profile = user.profile
			form = UserProfileForm(instance=profile)
		args = {}
		args.update(csrf(request))
		args['form'] = form
		args['user'] = request.user
		args['userinfo'] = UserProfile.objects.filter(user=User.objects.get(username=user_name))
		return render_to_response('editProfile.html', args)
	else:
		return HttpResponseRedirect('/')