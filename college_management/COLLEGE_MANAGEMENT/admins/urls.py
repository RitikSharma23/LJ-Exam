
from django.contrib import admin
from django.urls import path,include
from .views import *

uname='Admins'

urlpatterns = [
<<<<<<< HEAD
    path(f"{uname}-Dashboard/", dashboard, name=f"{uname}-Dashboard"),
=======
    path('dashboard/',dashboard),
    path('subadmin/',subadmin),
    path('subadmin-add/',subadminAdd),
    path('subadmin-edit/',subadminEdit),
    path('subject/',subject),
    path('subject-add/',subjectAdd),
    path('subject-edit/',subjectEdit),
    path('setting/',setting),
>>>>>>> f0739bc35721a5e71727adb74aee882de659ac6a
]
