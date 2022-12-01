from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("",adminpage),
    path("addinstitute/",addinstitute),
    path("doaddinstitute/",doaddinstitute),
    path("editinstitute/",editinstitute),
    path("doeditinstitute/",doeditinstitute),
    path("findinstitute/",findinstitute),
]