from django.shortcuts import render
from django.shortcuts import redirect

import pymongo
import json
from bson import json_util
from bson import ObjectId

mongo_uri = "mongodb+srv://ljexam:LjExam@ljexam.vysc2ku.mongodb.net/"

client = pymongo.MongoClient(mongo_uri)

database_name = "LJKU"
db = client[database_name]

def check_session(request):
    print("CHECKINF")
    if request.session.get('authenticated', False):
        return redirect('/login/')




def dashboard(request):
  check_session(request)
  session_data = request.session
  
  for key, value in session_data.items():
      print(f"Session Variable: {key}, Value: {value}")
  return render(request, 'SuperAdmin/dashboard.html',{})

def branch(request):
  
  collection = db["branch"]
  results = collection.find({})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[document['code']]=document
    
  return render(request, 'SuperAdmin/branch.html', {'data': data})


def branchAdd(request):
  return render(request, 'SuperAdmin/branch-add.html',{})

def branchEdit(request):
  collection = db["branch"]
  results = collection.find({'code':request.GET['id']})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document

  return render(request, 'SuperAdmin/branch-edit.html', {'data': data})

def branchAddPost(request):
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
  
  return redirect('/superadmin/branch/')

def branchEditPost(request):
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
  return redirect('/superadmin/branch/')

def branchDeletePost(request):
  print(request.GET)
  print(request.POST)
  collection = db["branch"]
  result = collection.delete_one({"_id":ObjectId(request.GET['id'])})
  print("Deleted Count:", result.deleted_count)
  return redirect('/superadmin/branch/')

def course(request):
  collection = db["course"]
  results = collection.find({})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[document['code']]=document
  return render(request, 'SuperAdmin/course.html',{'data':data})

def courseEdit(request):
  collection = db["course"]
  results = collection.find({'code':request.GET['id']})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document

  return render(request, 'SuperAdmin/course-edit.html',{'data':data})

def courseAdd(request):
  collection = db["branch"]
  results = collection.find({})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[document['code']]=document
  print(data)
  return render(request, 'SuperAdmin/course-add.html',{'data':data})


def courseAddPost(request):
  data=(request.POST)
  collection = db["course"]
  data_to_insert = {
     "code": data['code'],
     "name": data['name'],
     "sem": data['sem'],
     "year": data['year'],
     "branch": data['branch'],
     "email": data['email'],
     "phone": data['phone'],
  }
  result = collection.insert_one(data_to_insert)
  
  return redirect('/superadmin/course/')

def courseEditPost(request):
  data=(request.POST)
  collection = db["course"]
  data_to_insert = {"$set":{
     "code": data['code'],
     "name": data['name'],
     "sem": data['sem'],
     "year": data['year'],
     "email": data['email'],
     "phone": data['phone'],
  }}
  result = collection.update_one({"_id":ObjectId(request.POST['id'])}, data_to_insert) 
  return redirect('/superadmin/course/')

def courseDeletePost(request):
  print(request.GET)
  print(request.POST)
  collection = db["course"]
  result = collection.delete_one({"_id":ObjectId(request.GET['id'])})
  print("Deleted Count:", result.deleted_count)
  return redirect('/superadmin/course/')




def admins(request):
  collection = db["users"]
  results = collection.find({'role': 'Admin'})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data['data']=document
  return render(request, 'SuperAdmin/admins.html',{'data':data})

def adminsEdit(request):
  collection = db["users"]
  results = collection.find({'email':request.GET['id']})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document
    print(document)
  return render(request, 'SuperAdmin/admins-edit.html',{'data':data})

def adminsAdd(request):
  collection = db["branch"]
  results = collection.find({})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[document['code']]=document
  print(data)
  return render(request, 'SuperAdmin/admins-add.html',{'data':data})


def adminsAddPost(request):
  data=(request.POST)
  collection = db["users"]
  data_to_insert = {
     "fname": data['fname'],
     "lname": data['lname'],
     "address": data['address'],
     "branch": data['branch'],
     "email": data['email'],
     "phone": data['phone'],
     "password": 'nopass',
     "role": 'Admin',
  }
  result = collection.insert_one(data_to_insert)
  return redirect('/superadmin/admins/')

def adminsEditPost(request):
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
  return redirect('/superadmin/admins/')

def adminsDeletePost(request):
  print(request.GET)
  print(request.POST)
  collection = db["users"]
  result = collection.delete_one({"_id":ObjectId(request.GET['id'])})
  print("Deleted Count:", result.deleted_count)
  return redirect('/superadmin/admins/')




def setting(request):
  
  return render(request, 'SuperAdmin/setting.html',{})