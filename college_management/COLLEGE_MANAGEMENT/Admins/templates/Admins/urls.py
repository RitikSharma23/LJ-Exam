
from django.contrib import admin
from django.urls import path,include
from .views import *

u='Superadmin'

urlpatterns = [
    path(f"{u}-dashboard/", dashboard, name=f"{u}-dashboard"),
    path(f"{u}-calendar/", calendar, name=f"{u}-calendar"),

     path(f"{u}-profile/", profile, name=f"{u}-profile"),

     path(f"{u}-edit-profile/", profile_edit_GET, name=f"{u}-edit-profile"),
     path(f"{u}-edit-profile-post/", profile_edit_POST, name=f"{u}-edit-profile-post"),
    
    
    path(f"{u}-admins/", admins, name=f"{u}-admins"),
    path(f"{u}-add-admins/", addadmins_GET, name=f"{u}-add-admins"),
    path(f"{u}-add-admins-post/", addadmins_POST, name=f"{u}-admins-post"),
    
    path(f"{u}-edit-admins/", addadmins_edit_GET, name=f"{u}-edit-admins"),
    path(f"{u}-edit-admins-post/", addadmins_edit_POST, name=f"{u}-edit-admins-post"),
    path(f"{u}-delete-admins/", addadmins_delete_POST, name=f"{u}-delete-admins"),
    
    
    path(f"{u}-course/", course, name=f"{u}-course"),
    path(f"{u}-add-course/", addcourse_GET, name=f"{u}-add-course"),
    path(f"{u}-add-course-post/", addcourse_POST, name=f"{u}-course-post"),
    
    path(f"{u}-edit-course/", addcourse_edit_GET, name=f"{u}-edit-course"),
    path(f"{u}-edit-course-post/", addcourse_edit_POST, name=f"{u}-edit-course-post"),
    path(f"{u}-delete-course/", addcourse_delete_POST, name=f"{u}-delete-course"),
    
    
    
    path(f"{u}-branch/", branch, name=f"{u}-branch"),
    path(f"{u}-add-branch/", branch_GET, name=f"{u}-add-branch"),
    path(f"{u}-add-branch-post/", branch_POST, name=f"{u}-branch-post"),
    
    path(f"{u}-edit-branch/", branch_edit_GET, name=f"{u}-edit-branch"),
    path(f"{u}-edit-branch-post/", branch_edit_POST, name=f"{u}-edit-branch-post"),
    path(f"{u}-delete-branch/", branch_delete_POST, name=f"{u}-delete-branch"),
    
    
    
    path(f"{u}-inbox/", inbox, name=f"{u}-inbox"),
    path(f"{u}-read/", read, name=f"{u}-read"),
    path(f"testform/", testform, name="testform"),
    path(f"logout/", logout, name="logout"),
    
    
    
    
]
