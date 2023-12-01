
from django.contrib import admin
from django.urls import path,include
from .views import *

u='Subadmin'

urlpatterns = [
    path(f"{u}-dashboard/", dashboard, name=f"{u}-dashboard"),

    
    path(f"{u}-profile/", profile, name=f"{u}-profile"),
    path(f"{u}-edit-profile/", profile_edit_GET, name=f"{u}-edit-profile"),
    path(f"{u}-edit-profile-post/", profile_edit_POST, name=f"{u}-edit-profile-post"),


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


        
    path(f"{u}-exam/", exam, name=f"{u}-exam"),
    path(f"{u}-add-exam/", addexam_GET, name=f"{u}-add-exam"),
    path("insert_exam_POST/", insert_exam_POST, name="insert_exam_POST"),
    path(f"{u}-select-exam/", selectexam_GET, name=f"{u}-select-exam"),
    path(f"{u}-select-subject/", selectsubject_GET, name=f"{u}-select-subject"),
    path(f"{u}-add-exam-post/", addexam_POST, name=f"{u}-add-exam-post"),
    path(f"{u}-edit-exam/", addexam_edit_GET, name=f"{u}-edit-exam"),
    path(f"{u}-view-exam/", viewexam_edit_GET, name=f"{u}-view-exam"),
    path(f"{u}-close-exam/", closeexam_edit_GET, name=f"{u}-close-exam"),
    path(f"{u}-assign-exam/", assignexam_edit_GET, name=f"{u}-assign-exam"),
    path(f"{u}-edit-exam-post/", addexam_edit_POST, name=f"{u}-edit-exam-post"),
    path(f"{u}-delete-exam/", addexam_delete_POST, name=f"{u}-delete-exam"),


    path('upload_file/',upload_file,name="upload_file"),


]
