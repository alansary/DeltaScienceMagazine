from django.shortcuts import render_to_response

# Create your views here.

def alansary(request):
	return render_to_response('developer.html', {'user': request.user})