from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages


import pymongo
import json
from bson import json_util
from bson import ObjectId

mongo_uri = "mongodb+srv://ljexam:LjExam@ljexam.vysc2ku.mongodb.net/"
client = pymongo.MongoClient(mongo_uri)
database_name = "LJKU"
db = client[database_name]


def dashboard(request):
  return render(request,'Admin/dashboard.html',{})


def subadmin(request):
  collection = db["users"]
  results = collection.find({'role': 'Subadmin'})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data['data']=document
  return render(request,'Admin/subadmin.html',{'data':data})



def subadminEdit(request):
  collection = db["users"]
  results = collection.find({'email':request.GET['id']})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document
    print(document)
  return render(request, 'Admin/subadmin-edit.html',{'data':data})

def subadminAdd(request):
  collection = db["course"]
  results = collection.find({})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[document['code']]=document
  return render(request, 'Admin/subadmin-add.html',{'data':data})


def subadminAddPost(request):
  data=(request.POST)
  collection = db["users"]
  data_to_insert = {
     "fname": data['fname'],
     "lname": data['lname'],
     "address": data['address'],
     "branch": request.session.get('branch'),
     "course": data['course'],
     "email": data['email'],
     "phone": data['phone'],
     "password": data['phone'],
     "role": 'Subadmin',
  }
  result = collection.insert_one(data_to_insert)
  return redirect('/admins/subadmin/')

def subadminEditPost(request):
  data=(request.POST)
  collection = db["users"]
  data_to_insert = {"$set":{
     "fname": data['fname'],
     "lname": data['lname'],
     "address": data['address'],
     "branch": request.session.get('branch'),
     "email": data['email'],
     "phone": data['phone'],
     "password": data['phone'],
     "role": 'Subadmin',
  }}
  result = collection.update_one({"_id":ObjectId(request.POST['id'])}, data_to_insert) 
  return redirect('/Admin/subadmin/')

def subadminDeletePost(request):
  collection = db["users"]
  result = collection.delete_one({"_id":ObjectId(request.GET['id'])})
  print("Deleted Count:", result.deleted_count)
  return redirect('/Admin/subadmin/')



def subject(request):
  collection = db["subjects"]
  results = collection.find({})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[document['code']]=document
  return render(request,'Admin/subject.html',{'data':data})



def subjectEdit(request):
  collection = db["subjects"]
  results = collection.find({'subjectcode':request.GET['id']})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document
    print(document)
  return render(request, 'Admin/subject-edit.html',{'data':data})

def subjectAdd(request):
  collection = db["course"]
  results = collection.find({})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[document['code']]=document
  print(data)
  return render(request, 'Admin/subject-add.html',{'data':data})


def subjectAddPost(request):
  data=(request.POST)
  collection = db["subjects"]
  data_to_insert = {
     "name": data['name'],
     "code": data['code'],
     "course": data['course'],
     "sem": data['sem'],
     "branch": request.session.get('branch'),
  }
  result = collection.insert_one(data_to_insert)
  return redirect('/admins/subject/')

def subjectEditPost(request):
  data=(request.POST)
  collection = db["subjects"]
  data_to_insert = {"$set":{
     "fname": data['fname'],
     "lname": data['lname'],
     "address": data['address'],
     "branch": request.session.get('branch'),
     "email": data['email'],
     "phone": data['phone'],
     "password": data['phone'],
     "role": 'subject',
  }}
  result = collection.update_one({"_id":ObjectId(request.POST['id'])}, data_to_insert) 
  return redirect('/Admin/subject/')

def subjectDeletePost(request):
  collection = db["subjects"]
  result = collection.delete_one({"_id":ObjectId(request.GET['id'])})
  print("Deleted Count:", result.deleted_count)
  return redirect('/Admin/subject/')

