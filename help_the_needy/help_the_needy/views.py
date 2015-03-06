from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
	return render_to_response('index.html')

def map(request):
    loc = ''
    if request.method == 'POST':
        loc = request.POST.get('location', '')
    return render_to_response('display_map.html', {'location': loc}, context_instance=RequestContext(request))
