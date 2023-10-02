
from django.contrib import admin
from django.urls import path,include
from .views import *

u='Admins'

urlpatterns = [
    path(f"{u}-dashboard/", dashboard, name=f"{u}-dashboard"),
]
