from django.shortcuts import render
from .database_config import *

def home(request):
    print("Hello")
    return render(request,"home.html",{})
