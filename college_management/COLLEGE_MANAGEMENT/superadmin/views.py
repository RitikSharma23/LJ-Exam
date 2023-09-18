from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

import pymongo
import json
from bson import json_util
from bson import ObjectId

mongo_uri = "mongodb://localhost:27017"

client = pymongo.MongoClient(mongo_uri)

database_name = "LJKU"
db = client[database_name]





def dashboard(request):
  return render(request, 'dashboard.html',{})

def branch(request):
  collection = db["branch"]
  results = collection.find({})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[document['code']]=document
    
  return render(request, 'branch.html', {'data': data})


def branchAdd(request):
  return render(request, 'branch-add.html',{})

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
  
  return HttpResponseRedirect(reverse('branch'))

def branchEdit(request):
  collection = db["branch"]
  results = collection.find({'code':request.GET['id']})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document

  return render(request, 'branch-edit.html', {'data': data})

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
  return HttpResponseRedirect(reverse('branch'))

def branchDeletePost(request):
  print(request.GET)
  print(request.POST)
  collection = db["branch"]
  # result = collection.update_one({"_id":ObjectId(request.GET['id'])}, data_to_insert) 
  result = collection.delete_one({"_id":ObjectId(request.GET['id'])})
  print("Deleted Count:", result.deleted_count)
  return HttpResponseRedirect(reverse('branch'))

def course(request):
  
  return render(request, 'course.html',{})

def courseEdit(request):
  
  return render(request, 'course-edit.html',{})

def courseAdd(request):
  collection = db["branch"]
  results = collection.find({})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[document['code']]=document
  print(data)
  
  return render(request, 'course-add.html',{'data':data})

def admins(request):
  
  return render(request, 'admin.html',{})

def adminsAdd(request):
  
  return render(request, 'admin-add.html',{})

def adminsEdit(request):
  
  return render(request, 'admin-edit.html',{})

def setting(request):
  
  return render(request, 'setting.html',{})