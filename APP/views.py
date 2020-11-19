from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from APP import models
from django.views.decorators.csrf import csrf_exempt
# from dlib_fase import settings
import json
import base64
# from student import utils, form


def postural_Prediction(request):
    if request.method == "POST":

        print('xxxxx')
    return render(request, "postural_Prediction.html")