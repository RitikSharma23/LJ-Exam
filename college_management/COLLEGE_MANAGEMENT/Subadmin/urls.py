
from django.contrib import admin
from django.urls import path,include
from .views import *

u='Subadmin'

urlpatterns = [
    path(f"{u}-dashboard/", dashboard, name=f"{u}-dashboard"),
    path(f"{u}-profile/", profile, name=f"{u}-profile"),
    path(f"{u}-edit-profile/", profile_edit_GET, name=f"{u}-edit-profile"),
    path(f"{u}-faculty/", faculty, name=f"{u}-faculty"),
    path(f"{u}-add-faculty/", addfaculty_GET, name=f"{u}-add-faculty"),
    path(f"{u}-add-faculty-post/", addfaculty_POST, name=f"{u}-faculty-post"),
    path(f"{u}-edit-faculty/", addfaculty_edit_GET, name=f"{u}-edit-faculty"),
    path(f"{u}-edit-faculty-post/", addfaculty_edit_POST, name=f"{u}-edit-faculty-post"),
    path(f"{u}-delete-faculty/", addfaculty_delete_POST, name=f"{u}-delete-faculty"),

]
