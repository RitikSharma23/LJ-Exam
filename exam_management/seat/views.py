from django.shortcuts import render
from adminpage.models import *
# Create your views here.

def seathome(request):
    d=Subject.objects.all().values()
    details={'subjectlist':d}
    return render(request,"seat.html",details)

def adminpage(request):
    return render(request,"admin.html",{})