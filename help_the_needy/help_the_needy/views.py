from django.shortcuts import render_to_response
from django.template import RequestContext
from googleplaces import GooglePlaces

YOUR_API_KEY = 'AIzaSyAFjxvqADQeN985mvQuQQWnKKSUclu4HpI'

google_places = GooglePlaces(YOUR_API_KEY)

def home(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def map(request):
	ngos_name = []
	ngos_address = []
	ngos = {}
	loc = ""
	if request.method == 'POST':
		loc = request.POST.get('location', '')
	query_result = google_places.nearby_search(
			location=loc, keyword='ngos and non profit organizations',
			radius=20000)
	for place in query_result.places:
		place.get_details()
		ngos[place.name] = [place.formatted_address, place.local_phone_number, place.international_phone_number, place.url, place.website]
	return render_to_response('display_list2.html', {'location': loc, 'ngos':ngos}, context_instance=RequestContext(request))

