from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/',dashboard),
    path('subadmin/',subadmin),
    path('subadmin-add/',subadminAdd),
    path('subadmin-edit/',subadminEdit),
    path('subject/',subject),
    path('subject-add/',subjectAdd),
    path('subject-edit/',subjectEdit),
]
