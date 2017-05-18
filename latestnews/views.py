from django.shortcuts import render_to_response
from .models import New

# Create your views here.
def new(request, new_id):
	return render_to_response('new.html', {'new': New.objects.get(id=new_id), 'user': request.user})

def news(request):
	return render_to_response('news.html', {'news': New.objects.all(), 'user': request.user})

