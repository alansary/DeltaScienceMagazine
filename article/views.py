from django.shortcuts import render_to_response
from .models import Article, Comment, Department, ArticleLikes
from .forms import ArticleForm, CommentForm
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from deltasciencemagazine import settings

# Create your views here.
def departments(request):
	return render(request, 'departments.html', {'departments': Department.objects.all(), 'user': request.user})

def articles(request, dept_id=1):
	return render(request, 'articles.html', {'dept': Department.objects.get(id=dept_id), 'user': request.user})

def article(request, dept_id, article_id):
	a = Department.objects.get(id=dept_id).article_set.all().get(id=article_id)
	try:
		ArticleLikes.objects.get(article_id=article_id, user_id=request.user.id)
		label = "Unlike"
		up_down = "down"
	except:
		label = "Like"
		up_down = "up"
	c = {}
	c['dept'] = Department.objects.get(id=dept_id)
	c['article'] = a
	c['user'] = request.user
	c['label'] = label
	c['up_down'] = up_down
	return render(request, 'article.html', c)

@login_required
def create(request, dept_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/department/departments/%s' % dept_id)
	if request.POST:
		form = ArticleForm(request.POST, request.FILES)
		if form.is_valid():
			temp = form.save(commit=False)
			temp.department = Department.objects.get(id=dept_id)
			temp.pub_date = timezone.now()
			temp.username = request.user.username
			temp.save()
			messages.success(request, "Your article has been added to the system and will appear as soon as possible after checking its validity.")
			return HttpResponseRedirect('/department/departments/%s' % dept_id)
	else:
		form = ArticleForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	args['user'] = request.user
	args['dept'] = Department.objects.get(id=dept_id)
	args['currDate'] = timezone.now()
	return render_to_response('create.html', args)

@login_required
def like_article(request, dept_id, article_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/department/departments/%s/%s' % (dept_id, article_id))
	if article_id:
		a = Department.objects.get(id=dept_id).article_set.get(id=article_id)
		try:
			ArticleLikes.objects.get(article_id=article_id, user_id=request.user.id).delete()
			a.likes -= 1
		except:
			a.likes += 1
			ArticleLikes.objects.create(article_id=article_id, user_id=request.user.id)
		a.save()
	return HttpResponseRedirect('/department/departments/%s/%s' % (dept_id, article_id))

@login_required
def comment(request, dept_id, article_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/department/departments/%s/%s' % (dept_id, article_id))
	a = Department.objects.get(id=dept_id).article_set.get(id=article_id)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			temp = form.save(commit=False)
			temp.article = a
			temp.pub_date = timezone.now()
			temp.username = request.user.username
			temp.save()
			messages.success(request, "Your comment has been added successfully")
			return HttpResponseRedirect('/department/departments/%s/%s' % (dept_id, article_id))
	else:
		form = CommentForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	args['article'] = a
	args['user'] = request.user
	args['dept'] = Department.objects.get(id=dept_id)
	return render_to_response('add_comment.html', args)

@login_required
def deleteComment(request, dept_id, article_id, comment_id):
	c = Department.objects.get(id=dept_id).article_set.get(id=article_id).comment_set.get(id=comment_id)
	if request.user.is_authenticated and c.username == request.user.username:
		c.delete()
		messages.add_message(request,
			settings.DELETE_MESSAGE,
			"Your comment has been deleted successfully")
		return HttpResponseRedirect('/department/departments/%s/%s' % (dept_id, article_id))
	else:
		return HttpResponseRedirect('/department/departments/%s/%s' % (dept_id, article_id))
