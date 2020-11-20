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
    # user did provide email/password, now lets check database
    email_from_post = request.POST['email']
    password_from_post = request.POST['password']

    # this will return all users that have the email_from_post
    # in future we should require email to be unique
    users = User.objects.filter(email=email_from_post)
    if len(users) == 0:
        messages.error(request, "email/password does not exist")
        return redirect("/")

    user = users[0]
    print(user)

    if (user.password != password_from_post):
        messages.error(request, "email/password does not exist")
        return redirect("/")

    request.session['user_id'] = user.id

    return redirect("/register/view")


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
    print(user)
    return render(request, "view_home.html", context)


def view_articles(request):
    if 'user_id' not in request.session:
        return redirect('/')

    user = User.objects.get(id=request.session['user_id'])

    comment = Comment.objects.all().order_by('-created_at')

    context = {
        'user': user,
        'comment': comment
    }
    return render(request, "articles.html", context)


def make_post(request):

    errors = Comment.objects.add_comment_validator(request.POST)
    print(errors)

    if len(errors) > 0:
        for key, value in errors.items():
            error_msg = key + ' - ' + value
            messages.error(request, error_msg)
        return redirect('/articles')

    else:
        message_from_post = request.POST['message']
        uploaded_by_user = User.objects.get(id=request.session['user_id'])
        new_comment = Comment.objects.create(
            message=message_from_post,
            uploaded_by=uploaded_by_user
        )

        print(new_comment.id)
        request.session['comment_id'] = new_comment.id

        return redirect('/articles')
