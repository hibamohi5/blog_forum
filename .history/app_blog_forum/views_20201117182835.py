from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
