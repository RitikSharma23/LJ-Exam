
from django.contrib import admin
from django.urls import path,include
from .views import *

u='Student'

urlpatterns = [
    path(f"{u}-dashboard/", dashboard, name=f"{u}-dashboard"),
    path(f"{u}-profile/", profile, name=f"{u}-profile"),
]
