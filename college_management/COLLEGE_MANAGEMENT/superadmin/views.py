from django.shortcuts import render,redirect
import pymongo
import json
from bson import json_util
from bson import ObjectId

mongo_uri = "mongodb+srv://ljexam:LjExam@ljexam.vysc2ku.mongodb.net/"

client = pymongo.MongoClient(mongo_uri)

database_name = "LJKU"
db = client[database_name]

uname='Superadmin'


def dashboard(request):
  return render(request,f'{uname}/dashboard.html',{'title':'Dashboard'})

def admins(request):
  return render(request,f'{uname}/admins.html',{'title':'admins'})

def addadmins_GET(request):
  return render(request,f'{uname}/add-admins.html',{'title':'admins'})

def addadmins_POST(request):
  data=(request.POST)
  collection = db["users"]
  data_to_insert = {
     "fname": data['fname'],
     "lname": data['lname'],
     "address": data['address'],
     "branch": data['branch'],
     "email": data['email'],
     "phone": data['phone'],
     "password": data['phone'],
     "role": 'Admin',
  }
  result = collection.insert_one(data_to_insert)
  return redirect('/Superadmin-admins/')



def calendar(request):
  return render(request,f'{uname}/calendar.html',{'title':'calendar'})

def email(request):
  return render(request,f'{uname}/email.html',{'title':'email'})

def course(request):
  return render(request,f'{uname}/course.html',{'title':'course'})

def branch(request):
  return render(request,f'{uname}/branch.html',{'title':'branch'})


def inbox(request):
  return render(request,f'{uname}/inbox.html',{'title':'inbox'})

def read(request):
  return render(request,f'{uname}/read.html',{'title':'read'})

def testform(request):
  print(request.POST)
  
  return render(request,f'{uname}/read.html',{'title':'read'})

