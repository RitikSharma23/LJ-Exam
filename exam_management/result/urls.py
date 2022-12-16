from django.contrib import admin
from django.urls import path
from .views import *
from adminpage.urls import *
from adminpage.views import *

urlpatterns = [
    path("",resulthome),
    path("viewresult/",viewresult),
    path("addcourse/",addcourse),
    path("find/",find),
]