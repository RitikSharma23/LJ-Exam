
from django.contrib import admin
from django.urls import path,include
from .views import *

u='Subadmin'

urlpatterns = [
    path(f"{u}-dashboard/", dashboard, name=f"{u}-dashboard"),
    path(f"{u}-profile/", profile, name=f"{u}-profile"),
    path(f"{u}-edit-profile/", profile_edit_GET, name=f"{u}-edit-profile"),
    
    path(f"{u}-faculty/", faculty, name=f"{u}-faculty"),
    path(f"{u}-add-faculty/", addfaculty_GET, name=f"{u}-add-faculty"),
    path(f"{u}-add-faculty-post/", addfaculty_POST, name=f"{u}-faculty-post"),
    path(f"{u}-edit-faculty/", addfaculty_edit_GET, name=f"{u}-edit-faculty"),
    path(f"{u}-edit-faculty-post/", addfaculty_edit_POST, name=f"{u}-edit-faculty-post"),
    path(f"{u}-delete-faculty/", addfaculty_delete_POST, name=f"{u}-delete-faculty"),
    
    path(f"{u}-student/", student, name=f"{u}-student"),



    path("verify_aadhar/", verify_aadhar, name="verify_aadhar"),
    path("verify_email/", verify_email, name="verify_email"),
    path("verify_enroll/", verify_enroll, name="verify_enroll"),
    path("add_student_POST/", add_student_POST, name="add_student_POST"),
    path(f"{u}-add-student/", addstudent_GET, name=f"{u}-add-student"),

    path(f"{u}-add-student-post/", indaddstudent_POST, name=f"{u}-add-student-post"),
    path(f"{u}-edit-student/", addstudent_edit_GET, name=f"{u}-edit-student"),
    path(f"{u}-edit-student-post/", addstudent_edit_POST, name=f"{u}-edit-student-post"),
    path(f"{u}-delete-student/", addstudent_delete_POST, name=f"{u}-delete-student"),


    path('upload_file/',upload_file,name="upload_file"),


]
