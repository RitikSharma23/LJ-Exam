
from django.contrib import admin
from django.urls import path,include
from .views import *

u='Admins'

urlpatterns = [
    path(f"{u}-dashboard/", dashboard, name=f"{u}-dashboard"),
    path(f"{u}-calendar/", calendar, name=f"{u}-calendar"),
    path(f"{u}-email/", email, name=f"{u}-email"),
    
    path(f"{u}-subadmins/", subadmins, name=f"{u}-subadmins"),
    path(f"{u}-add-subadmins/", subadmins_GET, name=f"{u}-add-subadmins"),
    path(f"{u}-add-subadmins-post/", subadmins_POST, name=f"{u}-subadmins-post"),
    
    path(f"{u}-edit-subadmins/", subadmins_edit_GET, name=f"{u}-edit-subadmins"),
    path(f"{u}-edit-subadmins-post/", subadmins_edit_POST, name=f"{u}-edit-subadmins-post"),
    path(f"{u}-delete-subadmins/", subadmins_delete_POST, name=f"{u}-delete-subadmins"),
    
    
    path(f"{u}-subjects/", subjects, name=f"{u}-subjects"),
    path(f"{u}-add-subjects/", subjects_GET, name=f"{u}-add-subjects"),
    path(f"{u}-add-subjects-post/", subjects_POST, name=f"{u}-subjects-post"),
    
    path(f"{u}-edit-subjects/", subjects_edit_GET, name=f"{u}-edit-subjects"),
    path(f"{u}-edit-subjects-post/", subjects_edit_POST, name=f"{u}-edit-subjects-post"),
    path(f"{u}-delete-subjects/", subjects_delete_POST, name=f"{u}-delete-subjects"),
    
    
    
    path(f"{u}-marks/", marks, name=f"{u}-marks"),
    path(f"{u}-add-marks/", marks_GET, name=f"{u}-add-marks"),
    path(f"{u}-add-marks-post/", marks_POST, name=f"{u}-marks-post"),
    
    path(f"{u}-edit-marks/", marks_edit_GET, name=f"{u}-edit-marks"),
    path(f"{u}-edit-marks-post/", marks_edit_POST, name=f"{u}-edit-marks-post"),
    path(f"{u}-delete-marks/", marks_delete_POST, name=f"{u}-delete-marks"),
    
    
        
    path(f"{u}-exam/", exam, name=f"{u}-exam"),
    path(f"{u}-add-exam/", exam_GET, name=f"{u}-add-exam"),
    path(f"{u}-add-exam-post/", exam_POST, name=f"{u}-exam-post"),
    path(f"{u}-view-exam/", viewexam_edit_GET, name=f"{u}-view-exam"),
    path(f"{u}-reject-exam/", rejectexam_edit_GET, name=f"{u}-reject-exam"),
    path(f"{u}-approve-exam/", approveexam_edit_GET, name=f"{u}-approve-exam"),

    
    path(f"{u}-edit-exam/", exam_edit_GET, name=f"{u}-edit-exam"),
    path(f"{u}-edit-exam-post/", exam_edit_POST, name=f"{u}-edit-exam-post"),
    path(f"{u}-delete-exam/", exam_delete_POST, name=f"{u}-delete-exam"),
    
    
    
    path(f"{u}-inbox/", inbox, name=f"{u}-inbox"),
    path(f"{u}-read/", read, name=f"{u}-read"),
    path(f"testform/", testform, name="testform"),
    path(f"logout/", logout, name="logout"),
    
    
    
    
]
