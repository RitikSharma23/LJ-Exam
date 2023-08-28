from django.contrib import admin
from django.urls import path,include
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', home),
    path("home/post-login/",csrf_exempt(login_with_email_password)),
    
]