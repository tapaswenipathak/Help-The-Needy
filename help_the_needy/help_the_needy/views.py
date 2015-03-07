from django.shortcuts import render_to_response
from django.template import RequestContext
from googleplaces import GooglePlaces

YOUR_API_KEY = 'AIzaSyBxyEeoSD4AiuaAOW5MWJgUwEJkdHEN6xs'

google_places = GooglePlaces(YOUR_API_KEY)

def home(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def map(request):
	print("map is called \o/")
	ngos_name = {'NGO1':'abcbcbc', 'NGO2':'uuuuuu'}
	ngos_address = {}
	loc = ""
	if request.method == 'POST':
		loc = request.POST.get('location', '')
		print("Inside map ", loc)
	# query_result = google_places.nearby_search(
	# 		location=loc, keyword='ngos and non profit organizations',
	# 		radius=20000)
	# print("heeeeeeeeeeeeeeeeeeeeeeeeeeeere is query_result", query_result.places)
	# for place in query_result.places:
	# 	#place.get_details()
	# 	print place.name, place.geo_location, place.reference
	# 	#print place.formatted_address
	# 	ngos_name.append(place.name)
	# 	#print place.geo_location
	return render_to_response('display_map.html', {'location': loc, 'ngos_name':ngos_name}, context_instance=RequestContext(request))

def map2(request):
	loc = request.POST.get('location', '')
	print("map 2 called :D ", loc)
	return render_to_response('display_map2.html', {'location':loc})
