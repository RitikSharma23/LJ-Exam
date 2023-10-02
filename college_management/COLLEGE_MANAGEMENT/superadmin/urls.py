
from django.contrib import admin
from django.urls import path,include
from .views import *

u='Superadmin'

urlpatterns = [
    path(f"{u}-dashboard/", dashboard, name=f"{u}-dashboard"),
    path(f"{u}-calendar/", calendar, name=f"{u}-calendar"),
    path(f"{u}-email/", email, name=f"{u}-email"),
    
    path(f"{u}-admins/", admins, name=f"{u}-admins"),
    path(f"{u}-add-admins/", addadmins_GET, name=f"{u}-add-admins"),
    path(f"{u}-add-admins-post/", addadmins_POST, name=f"{u}-admins-post"),
    # path(f"{u}-add-admins-get/", addadmins_GET, name=f"{u}-admins-get"),
    
    path(f"{u}-course/", course, name=f"{u}-course"),
    path(f"{u}-branch/", branch, name=f"{u}-branch"),
    path(f"{u}-inbox/", inbox, name=f"{u}-inbox"),
    path(f"{u}-read/", read, name=f"{u}-read"),
    path(f"testform/", testform, name="testform"),
    
    
    
    
]
