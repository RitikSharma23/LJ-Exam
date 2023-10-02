
from django.contrib import admin
from django.urls import path,include
from .views import *

uname='Faculty'

urlpatterns = [
    path(f"{uname}-Dashboard/", dashboard, name=f"{uname}-Dashboard"),
]
