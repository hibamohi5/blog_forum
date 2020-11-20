from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    return render(request, "index.html")

def register_new_user(request):

    errors = User.objects.user_registration_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            error_msg = key + ' - ' + value
            messages.error(request, error_msg)

        return redirect("/")

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
        print(new_user.id)
        request.session['user_id'] = new_user.id

        return redirect('/register/view')

def login(request):
    email_from_post = request.POST['email']
    password_from_post = request.POST['password']

    users = User.objects.filter(email=email_from_post)

    

def logout(request):
    request.session.clear()
    return redirect("/")

def view_home(request):
    if 'user_id' not in request.session:
        return redirect("/")

    user = User.objects.get(id=request.session['user_id'])
    context = {
        "user": user
    }
    return render(request, "view_home.html", context)
