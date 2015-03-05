from django.shortcuts import render_to_response

def map(request):
    return render_to_response("display_map.html")