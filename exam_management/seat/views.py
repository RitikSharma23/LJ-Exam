from django.shortcuts import render

# Create your views here.

def seathome(request):
    return render(request,"seat.html",{})

def adminpage(request):
    return render(request,"admin.html",{})