from django.shortcuts import render_to_response
from .models import Year, Volume, Paper, Highlight, Author, MostPopularPaper
from carousel.models import Carousel, ActiveCarousel

# Create your views here.
def volumes(request):
	context = {}
	context['years'] = Year.objects.all()
	context['carousels'] = Carousel.objects.all()
	context['activeCarousel'] = ActiveCarousel.objects.all()
	context['mostPopular'] = MostPopularPaper.objects.all()
	context['user'] = request.user
	return render_to_response('volumes.html', context)

def volume(request, year_id, volume_id):
	context = {}
	context['volume'] = Year.objects.get(id=year_id).volume_set.get(id=volume_id)
	context['year_id'] = year_id
	context['volume_id'] = volume_id
	context['carousels'] = Carousel.objects.all()
	context['activeCarousel'] = ActiveCarousel.objects.all()
	context['years'] = Year.objects.all()
	context['user'] = request.user
	return render_to_response('volume.html', context)

def paper(request, year_id, volume_id, paper_id):
	context = {}
	context['carousels'] = Carousel.objects.all()
	context['activeCarousel'] = ActiveCarousel.objects.all()
	context['year_id'] = year_id
	context['volume_id'] = volume_id
	context['paper_id'] = paper_id
	context['years'] = Year.objects.all()
	context['volume'] = Year.objects.get(id=year_id).volume_set.get(id=volume_id)
	context['paper'] = Year.objects.get(id=year_id).volume_set.all().get(id=volume_id).paper_set.all().get(id=paper_id)
	context['user'] = request.user
	return render_to_response('paper.html', context)
