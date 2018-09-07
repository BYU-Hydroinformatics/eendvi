from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button
from django.http import JsonResponse, HttpResponse, Http404
import datetime
import json
from eeutils import *

def home(request):
    """
    Controller for the app home page.
    """


    context = {

    }

    return render(request, 'ndvi/home.html', context)

def get_plot(request):
    return_obj = {}
    context = {}

    if request.is_ajax() and request.method == 'POST':
        info = request.POST

        polygon = request.POST['polygon']

        polygon = json.loads(polygon)

        if polygon:
            try:
                ee_obj = executeNDVI(polygon['coordinates'])

                return_obj["ee_obj"] = ee_obj
                return_obj["success"] = "success"
                return JsonResponse(return_obj)

            except Exception as e:
                return_obj["error"] = "Error Retrieving Data"
                return JsonResponse(return_obj)