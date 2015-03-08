from django.shortcuts import render_to_response
from django.template import RequestContext
from googleplaces import GooglePlaces

YOUR_API_KEY = 'AIzaSyBxyEeoSD4AiuaAOW5MWJgUwEJkdHEN6xs'

google_places = GooglePlaces(YOUR_API_KEY)

def home(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def map(request):
	# ngos_name = {'NGO1':'abcbcbc', 'NGO2':'uuuuuu', 'NGO3':"thierd one"}
	ngos_name = []
	ngos_address = []
	ngos = {}
	loc = ""
	if request.method == 'POST':
		loc = request.POST.get('location', '')
		print("Inside map ", loc)
	query_result = google_places.nearby_search(
			location=loc, keyword='ngos and non profit organizations',
			radius=20000)
	print("query_result is gnerated! length  of places = ", len(query_result.places))
	for place in query_result.places:
		place.get_details()
		print(place.name, place.formatted_address, place.local_phone_number, place.url)
		ngos[place.name] = [place.formatted_address, place.local_phone_number, place.international_phone_number, place.url, place.website]
	print("Here is our dict")
	print(ngos)
	return render_to_response('display_list2.html', {'location': loc, 'ngos':ngos}, context_instance=RequestContext(request))

def map2(request):
	loc = request.POST.get('location', '')
	print("map 2 called :D ", loc)
	return render_to_response('display_map2.html', {'location':loc})
