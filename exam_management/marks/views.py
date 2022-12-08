from django.shortcuts import render,HttpResponse
from adminpage.models import *

# Create your views here.

def markshome(request):
    d=Subject.objects.all().values()
    details={'subjectlist':d}
    return render(request,"marks.html",details)

def adminpage(request):
    return render(request,"admin.html",{})

def marksoption(request):
    data=request.POST
    print(data)
    d=Subject.objects.filter(subjectcode=data['subjectcode']).values()
    details={'subject':d[0],'year':data['year']}
    return render(request,"marksoption.html",details)