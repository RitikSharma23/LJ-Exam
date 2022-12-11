from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("",markshome),
    path("marksoption/",marksoption),
    path("theory/",theory),
    path("practical/",practical),
    path("mid/",mid),
    
    path("uploadtheory/",uploadtheory),
    path("submittheory/",submittheory),

    path("uploadpractical/",uploadpractical),
    path("submitpractical/",submitpractical),

    path("uploadmid/",uploadmid),
    path("submitmid/",submitmid),
]