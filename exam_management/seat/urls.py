from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("",seathome),
    path("seatoption/",seatoption),
    path("remedial/",remedial),
    path("seatsem/",seatsem),
    path("seatremedial/",seatremedial),
    path("downloadseat/",downloadseat),
]