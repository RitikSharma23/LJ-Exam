from django.shortcuts import render,redirect
import pymongo
import json
from bson import json_util
from bson import ObjectId
from django.contrib.sessions.models import Session


mongo_uri = "mongodb+srv://ljexam:LjExam@ljexam.vysc2ku.mongodb.net/"

client = pymongo.MongoClient(mongo_uri)

database_name = "LJKU"
db = client[database_name]

uname='Superadmin'

def getbranch():
  collection = db["branch"]
  results = collection.find()
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[str(document['_id'])]=document
  return data
  


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
  branch=getbranch()
  return render(request,f'{uname}/add-admins.html',{'title':'admins','branch':branch})

def addadmins_POST(request):
  data=(request.POST)
  collection = db["users"]
  data_to_insert = {
     "fname": data['fname'],
     "lname": data['lname'],
     "address": data['address'],
     "branch": data['branch'],
     "course": '000',
     "email": data['email'],
     "phone": data['phone'],
     "password": data['phone'],
     "role": 'Admin',
     "profile_pic":'https://static.vecteezy.com/system/resources/thumbnails/009/734/564/small/default-avatar-profile-icon-of-social-media-user-vector.jpg',
     
  }
  result = collection.insert_one(data_to_insert)
  return redirect('/Superadmin-admins/')

def addadmins_edit_GET(request):
  collection = db["users"]
  results = collection.find({'_id':ObjectId(request.GET['id'])})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document
  branch=getbranch()
  return render(request,f'{uname}/edit-admins.html',{'title':'admins','data':data,'branch':branch})


def addadmins_edit_POST(request):
  data=(request.POST)
  collection = db["users"]
  data_to_insert = {"$set":{
     "fname": data['fname'],
     "lname": data['lname'],
     "address": data['address'],
     "email": data['email'],
     "phone": data['phone'],
     "branch": data['branch'],
  }}
  result = collection.update_one({"_id":ObjectId(request.POST['id'])}, data_to_insert) 
  return redirect('/Superadmin-admins/')


def addadmins_delete_POST(request):
  collection = db["users"]
  result = collection.delete_one({"_id":ObjectId(request.GET['id'])})
  print("Deleted Count:", result.deleted_count)
  return redirect('/Superadmin-admins/')




def calendar(request):
  return render(request,f'{uname}/calendar.html',{'title':'calendar'})

def email(request):
  return render(request,f'{uname}/email.html',{'title':'email'})

def profile(request):
  collection = db["users"]
  results = collection.find({'email':request.session.get("email")})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document
  return render(request,f'{uname}/profile.html',{'title':'profile','data':data})





def profile_edit_GET(request):
  
  collection = db["users"]
  results = collection.find({'email':request.session.get("email")})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document


  return render(request,f'{uname}/edit-profile.html',{'title':'edit-profile','data':data})


def profile_edit_POST(request):
  
  data=(request.POST)
  collection = db["users"]
  data_to_insert = {"$set":{
     "fname": data['fname'],
     "lname": data['lname'],
     "address": data['address'],
     "email": data['email'],
     "phone": data['phone'],
     
  }}
  result = collection.update_one({"_id":ObjectId(request.POST['id'])}, data_to_insert) 
  return redirect('/Superadmin-profile/')








def course(request):
  collection = db["course"]
  results = collection.find()
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[str(document['_id'])]=document
  return render(request,f'{uname}/course.html',{'title':'course','data':data})

def addcourse_GET(request):
  branch=getbranch()
  return render(request,f'{uname}/add-course.html',{'title':'course','branch':branch})

def addcourse_POST(request):
  data=(request.POST)
  collection = db["course"]
  data_to_insert = {
     "name": data['name'],
     "code": data['code'],
     "email": data['email'],
     "phone": data['phone'],
     "branch": data['branchs'],
     "type": data['type'],
     "year": data['year'],
     "sem": data['sem'],
  }
  result = collection.insert_one(data_to_insert)
  return redirect('/Superadmin-course/')

def addcourse_edit_GET(request):
  collection = db["course"]
  results = collection.find({'_id':ObjectId(request.GET['id'])})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document
  branch=getbranch()

  return render(request,f'{uname}/edit-course.html',{'title':'course','data':data,'branch':branch})


def addcourse_edit_POST(request):
  data=(request.POST)
  collection = db["course"]
  data_to_insert = {"$set":{
     "name": data['name'],
     "code": data['code'],
     "email": data['email'],
     "phone": data['phone'],
     "branch": data['branch'],
     "type": data['type'],
     "year": data['year'],
     "sem": data['sem'],
  }}
  result = collection.update_one({"_id":ObjectId(request.POST['id'])}, data_to_insert) 
  return redirect('/Superadmin-course/')


def addcourse_delete_POST(request):
  collection = db["course"]
  result = collection.delete_one({"_id":ObjectId(request.GET['id'])})
  print("Deleted Count:", result.deleted_count)
  return redirect('/Superadmin-course/')












def branch(request):
  collection = db["branch"]
  results = collection.find()
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[str(document['_id'])]=document
  return render(request,f'{uname}/branch.html',{'title':'branch','data':data})

def branch_GET(request):
  return render(request,f'{uname}/add-branch.html',{'title':'branch'})

def branch_POST(request):
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

def branch_edit_GET(request):
  collection = db["branch"]
  results = collection.find({'_id':ObjectId(request.GET['id'])})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document

  return render(request,f'{uname}/edit-branch.html',{'title':'branch','data':data})


def branch_edit_POST(request):
  data=(request.POST)
  collection = db["branch"]
  data_to_insert = {"$set":{
     "code": data['code'],
     "name": data['name'],
     "email": data['email'],
     "phone": data['phone'],
     "address": data['address'],
  }}
  result = collection.update_one({"_id":ObjectId(request.POST['id'])}, data_to_insert) 
  return redirect('/Superadmin-branch/')


def branch_delete_POST(request):
  collection = db["branch"]
  result = collection.delete_one({"_id":ObjectId(request.GET['id'])})
  print("Deleted Count:", result.deleted_count)
  return redirect('/Superadmin-branch/')



  





def inbox(request):
  return render(request,f'{uname}/inbox.html',{'title':'inbox'})

def read(request):
  return render(request,f'{uname}/read.html',{'title':'read'})

def testform(request):
  print(request.POST)
  
  return render(request,f'{uname}/read.html',{'title':'read'})



def logout(request):
  print("superadmin logout")
  if request.session.get('is_authenticated', False):
    request.session.clear() 
    request.session['is_authenticated'] = True
    request.session.save()
     
  return redirect('/') 

