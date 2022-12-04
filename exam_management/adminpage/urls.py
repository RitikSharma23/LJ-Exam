from django.contrib import admin
from django.urls import path
from .views import *
from .student import *

urlpatterns = [
    path("",adminpage),
    path("addinstitute/",addinstitute),
    path("doaddinstitute/",doaddinstitute),
    path("editinstitute/",editinstitute),
    path("doeditinstitute/",doeditinstitute),
    path("doaddstudent/",doaddstudent),
    path("findinstitute/",findinstitute),
    path("addstudent/",addstudent),
    path("addcourse/",addcourse),
    path("clear/",clear),
]