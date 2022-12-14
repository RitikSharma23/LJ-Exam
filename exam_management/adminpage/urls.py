from django.contrib import admin
from django.urls import path
from .views import *
from .student import *

urlpatterns = [
    path("",adminpage),
    path("addinstitute/",addinstitute),
    path("doaddinstitute/",doaddinstitute),
    path("editinstitute/",editinstitute),
    path("editstudent/",editstudent),
    path("doeditstudent/",doeditstudent),
    path("doeditinstitute/",doeditinstitute),
    path("doaddstudent/",doaddstudent),
    path("findinstitute/",findinstitute),
    path("findstudent/",findstudent),
    path("deleteinstitute/",deleteinstitute),
    path("addstudent/",addstudent),
    path("addcourse/",addcourse),
    path("clear/",clear),
    path("selectexcel/",selectexcel),
    path("generateexcel/",generateexcel),
    path("downloadexcel/",downloadexcel),
    path("uploadexcel/",uploadexcel),
    path("addsubject/",addsubject),
    path("viewsubject/",viewsubject),
    path("doaddsubject/",doaddsubject),
    path("editsubject/",editsubject),
    path("doeditsubject/",doeditsubject),
    path("upgradepage/",upgradepage),
    path("upgradebatch/",upgradebatch),
]