from django.shortcuts import render,HttpResponse
from adminpage.models import *
# Create your views here.

def seathome(request):
    d=Subject.objects.all().values()
    details={'subjectlist':d}
    return render(request,"seat.html",details)

def seatoption(request):
    data=request.POST
    d=Subject.objects.filter(subjectcode=data['subjectcode']).values()
    print(d)
    details={
        'data':data,
        'subject':d[0]
    }
    return render(request,"seatoption.html",details)

def remedial(request):1

def adminpage(request):
    return render(request,"admin.html",{})