from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('login/',login,name="login"),
    path('logout/',logout,name="logout"),
    path('post-login/',postLogin,name="post-login"),
    path('reset-password/',passwordReset,name="reset-password"),
    path('forgot-password-page/',passpage,name="forgot-password-page"),
    path('postforgot/',postforgot,name="postforgot"),
    path('post-reset/',postreset,name="post-reset"),
    path('upload_file/',upload_file,name="upload_file"),
    path('testpage/',testpage,name="testpage"),
    path('generate_pdf/', generate_pdf, name='generate_pdf'),
]
