from django.shortcuts import render


def home(request):
    return render(request,"home.html",{})

def login(request):
    return render(request,"login.html",{})

def post_login(request):
    data=request.POST
    print(data)
    return render(request,"login.html",{})









