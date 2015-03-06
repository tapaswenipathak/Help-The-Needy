from django.shortcuts import render_to_response
from django.template import RequestContext
from googleplaces import GooglePlaces

YOUR_API_KEY = 'AIzaSyAFjxvqADQeN985mvQuQQWnKKSUclu4HpI'

google_places = GooglePlaces(YOUR_API_KEY)

def home(request):
	return render_to_response('index.html')

def map(request):
	ngos = []
	loc = ""
	if request.method == 'POST':
		loc = request.POST.get('location', '')
	query_result = google_places.nearby_search(
			location="Delhi", keyword='ngos and non profit organizations',
			radius=20000)
	if query_result.has_attributions:
		print query_result.html_attributions
	for place in query_result.places:
		print place.name
		ngos.append (place.name)
		print place.geo_location
	return render_to_response('display_map.html', {'location': ngos}, context_instance=RequestContext(request))
