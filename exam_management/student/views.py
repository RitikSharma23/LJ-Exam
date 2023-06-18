from django.shortcuts import render

# Create your views here.

def student(request):
    return render(request,"student.html",{})

def adminpage(request):
    return render(request,"admin.html",{})