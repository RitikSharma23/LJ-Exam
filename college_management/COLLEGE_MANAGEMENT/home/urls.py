from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('login/',login,name="login"),
    path('logout/',logout,name="logout"),
    path('post-login/',postLogin,name="post-login"),
]
