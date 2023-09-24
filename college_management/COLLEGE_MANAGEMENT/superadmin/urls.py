from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/',dashboard),
    path('branch/',branch),
    path('branch-add/',branchAdd),
    path('branch-add-post/',branchAddPost),
    path('branch-edit/',branchEdit),
    path('branch-edit-post/',branchEditPost),
    path('branch-delete-post/',branchDeletePost),
    
    
    path('course/',course),
    path('course-add/',courseAdd),
    path('course-edit/',courseEdit),
    
    
    path('admin/',admins),
    path('admin-add/',adminsAdd),
    path('admin-edit/',adminsEdit),
    
    
    path('setting/',setting),
]
