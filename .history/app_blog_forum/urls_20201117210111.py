from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),

    path('register', views.register_new_user),
    path('logout', views.logout),
    path('login', views.view_home),


    #this puts user on path to render new html home
    path('register/view', views.view_home),
    path('articles', views.view_articles)
]
