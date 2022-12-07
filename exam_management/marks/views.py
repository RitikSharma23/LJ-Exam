from django.shortcuts import render

# Create your views here.

def markshome(request):
    return render(request,"marks.html",{})

def adminpage(request):
    return render(request,"admin.html",{})