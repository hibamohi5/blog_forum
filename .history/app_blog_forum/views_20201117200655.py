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
    
    else:
        first_name_from_post = request.POST['first_name']
        last_name_from_post = request.POST['last_name']
        email_from_post = request.POST['email']
        password_from_post = request.POST['password']
        new_user = User.objects.create(
            first_name=first_name_from_post,
            last_name=last_name_from_post,
            email=email_from_post,
            password=password_from_post
        )
        print(new_user_)