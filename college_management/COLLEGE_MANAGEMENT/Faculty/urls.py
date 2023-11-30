
from django.contrib import admin
from django.urls import path,include
from .views import *

u='Faculty'

urlpatterns = [
    path(f"{u}-dashboard/", dashboard, name=f"{u}-dashboard"),
    path(f"{u}-profile/", profile, name=f"{u}-profile"),
    path(f"{u}-marksentry/", marksentry, name=f"{u}-marksentry"),
    path(f"{u}-generatseat/", generateseat, name=f"{u}-generateseat"),

    path(f"{u}-edit-profile/", profile_edit_GET, name=f"{u}-edit-profile"),
    path(f"{u}-enter-marks/", entermarks_GET, name=f"{u}-enter-marks"),
    path('update_marks/<str:document_id>/', update_marks, name='update_marks'),




]
