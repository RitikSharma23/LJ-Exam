from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/',dashboard,name="dashboard"),
    path('branch/',branch,name="branch"),
    path('branch-add/',branchAdd,name="branch-add"),
    path('branch-add-post/',branchAddPost,name="branch-add-post"),
    path('branch-edit/',branchEdit,name="branch-edit"),
    path('branch-edit-post/',branchEditPost,name="branch-edit-post"),
    path('branch-delete-post/',branchDeletePost,name="branch-delete-post"),
    
    
    path('course/',course,name="course"),
    path('course-add/',courseAdd,name="course-add"),
    path('course-edit/',courseEdit,name="course-edit"),
    
    
    path('admin/',admins,name="admin"),
    path('admin-add/',adminsAdd,name="admin-add"),
    path('admin-edit/',adminsEdit,name="admin-edit"),
    
    
    path('setting/',setting,name="setting"),
]
