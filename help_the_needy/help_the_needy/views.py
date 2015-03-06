from django.shortcuts import render_to_response
from django.template import RequestContext
# from googleplaces import GooglePlaces

# YOUR_API_KEY = 'AIzaSyAFjxvqADQeN985mvQuQQWnKKSUclu4HpI'

# google_places = GooglePlaces(YOUR_API_KEY)

def home(request):
	return render_to_response('index.html')

def map2(request):
    loc = ''
    if request.method == 'POST':
	    loc = request.POST.get('location', '')
    return render_to_response('display_map2.html', {'location': loc}, context_instance=RequestContext(request))	
