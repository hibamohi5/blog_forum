from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
