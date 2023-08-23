from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("",home),
    path("home/",home),
    path("login/",login),
    path("login/post-login/",post_login),
]