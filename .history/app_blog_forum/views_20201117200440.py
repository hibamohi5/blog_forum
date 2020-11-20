from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    return render(request, "index.html")

def register_new_user(request):
    errors = User.objects.user_registration_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors():
            error_msg = key + ' - ' + value
            messages.error(request, error_msg)
        
        return redirect('/')
    