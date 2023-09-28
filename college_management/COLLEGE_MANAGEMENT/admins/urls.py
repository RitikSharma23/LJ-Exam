from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/',dashboard),
    
    
    path('subadmin/',subadmin),
    path('subadmin-add/',subadminAdd),
    path('subadmin-edit/',subadminEdit),
    path('subadmins-add-post/',subadminAddPost),
    path('subadmin-edit-post/',subadminEditPost),
    path('subadmin-delete-post/',subadminDeletePost),
    
    
    path('subject/',subject),
    path('subject-add/',subjectAdd),
    path('subject-edit/',subjectEdit),
    path('subject-add-post/',subjectAddPost),
    path('subject-edit-post/',subjectEditPost),
    path('subject-delete-post/',subjectDeletePost),
]
