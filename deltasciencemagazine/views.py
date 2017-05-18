from django.shortcuts import render_to_response, render
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from django.contrib import auth
from .forms import AlansaryCreationForm
from carousel.models import Carousel, ActiveCarousel
from article.models import MostPopular
from latestnews.models import New 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home_page(request):
	context = {}
	context['user'] = request.user
	context['carousels'] = Carousel.objects.all()
	context['activeCarousel'] = ActiveCarousel.objects.all()
	context['mostPopular'] = MostPopular.objects.all()
	context['news'] = New.objects.all()
	return render(request, 'base.html', context)

def login_view(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/success_login')
	else:
		return HttpResponseRedirect('/accounts/invalid_login')

@login_required
def success_login(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	return HttpResponseRedirect('/')

def invalid_login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	return render_to_response('invalid_login.html')

@login_required
def logout_user(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	auth.logout(request)
	return HttpResponseRedirect('/')

def successful_register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	return render(request, 'successful_register.html')

def register_user(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/')
	if request.method == 'POST':
		form = AlansaryCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Your account has been created")
			return HttpResponseRedirect('/')
	args = {}
	args.update(csrf(request))
	args['form'] = AlansaryCreationForm()
	return render_to_response('register_user.html', args)