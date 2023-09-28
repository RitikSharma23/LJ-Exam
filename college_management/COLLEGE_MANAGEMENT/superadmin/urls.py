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
    path('course-add-post/',courseAddPost),
    path('course-edit-post/',courseEditPost),
    path('course-delete-post/',courseDeletePost),
    
    
    path('admins/',admins),
    path('admins-add/',adminsAdd),
    path('admins-edit/',adminsEdit),
    path('admins-add-post/',adminsAddPost),
    path('admins-edit-post/',adminsEditPost),
    path('admins-delete-post/',adminsDeletePost),
    
    
    
    path('setting/',setting),
]
