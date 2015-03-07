from django.shortcuts import render_to_response
from django.template import RequestContext
from googleplaces import GooglePlaces

YOUR_API_KEY = 'AIzaSyAFjxvqADQeN985mvQuQQWnKKSUclu4HpI'

google_places = GooglePlaces(YOUR_API_KEY)

def home(request):
	return render_to_response('index.html')

def map(request):
	ngos_name = []
	loc = ""
	if request.method == 'POST':
		loc = request.POST.get('location', '')
		print loc
	query_result = google_places.nearby_search(
			location="Dilshad Garden", keyword='ngos and non profit organizations',
			radius=20000)
	for place in query_result.places:
		#place.get_details()
		print place.name
		#print place.formatted_address
		ngos_name.append(place.name)
		#print place.geo_location
	return render_to_response('display_list.html', {'location': ngos_name}, context_instance=RequestContext(request))
