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
  collection = db["users"]
  results = collection.find({'role': 'Admin'})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[str(document['_id'])]=document
  return render(request,f'{uname}/admins.html',{'title':'admins','data':data})

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


def addbranch_GET(request):
  return render(request,f'{uname}/add-branch.html',{'title':'branch'})



def addbranch_POST(request):
  data=(request.POST)
  collection = db["branch"]
  data_to_insert = {
     "code": data['code'],
     "name": data['name'],
     "email": data['email'],
     "phone": data['phone'],
     "address": data['address'],
  }
  result = collection.insert_one(data_to_insert)
  return redirect('/Superadmin-branch/')
  





def inbox(request):
  return render(request,f'{uname}/inbox.html',{'title':'inbox'})

def read(request):
  return render(request,f'{uname}/read.html',{'title':'read'})

def testform(request):
  print(request.POST)
  
  return render(request,f'{uname}/read.html',{'title':'read'})

