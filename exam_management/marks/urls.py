from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("",markshome),
    path("marksoption/",marksoption),
    path("theory/",theory),
    path("uploadtheory/",uploadtheory),
    path("submittheory/",submittheory),
]