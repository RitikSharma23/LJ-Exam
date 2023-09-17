from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/',dashboard,name="dashboard"),
    path('branch/',branch,name="branch"),
    path('branch-add/',branchAdd,name="branch-add"),
    path('branch-edit/',branchEdit,name="branch-edit"),
    path('course/',course,name="course"),
    path('course-add/',courseAdd,name="course-add"),
    path('course-edit/',courseEdit,name="course-edit"),
    path('admin/',admins,name="admin"),
    path('admin-add/',adminsAdd,name="admin-add"),
    path('admin-edit/',adminsEdit,name="admin-edit"),
    path('setting/',setting,name="setting"),
]
