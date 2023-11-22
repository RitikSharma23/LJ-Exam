
from django.shortcuts import render,redirect
import pymongo
import json
from bson import json_util
from bson import ObjectId
from django.contrib.sessions.models import Session

# Create your views here.



mongo_uri = "mongodb+srv://ljexam:LjExam@ljexam.vysc2ku.mongodb.net/"

client = pymongo.MongoClient(mongo_uri)

database_name = "LJKU"
db = client[database_name]

uname='Subadmin'


def dashboard(request):
  return render(request,f'{uname}/dashboard.html',{'title':'Dashboard'})



def profile(request):
  return render(request,f'{uname}/profile.html',{'title':'profile'})


def profile_edit_GET(request):
  
  return render(request,f'{uname}/edit-profile.html',{'title':'edit-profile'})



def faculty(request):
  collection = db["users"]
  results = collection.find({'role': 'Faculty'})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[str(document['_id'])]=document
  return render(request,f'{uname}/faculty.html',{'title':'faculty','data':data})

def getbranch():
  collection = db["branch"]
  results = collection.find()
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[str(document['_id'])]=document
  return data





def addfaculty_GET(request):
  branch=getbranch()
  
  return render(request,f'{uname}/add-faculty.html',{'title':'faculty','branch':branch})

def addfaculty_POST(request):
  data=(request.POST)
  collection = db["users"]
  data_to_insert = {
     "fname": data['fname'],
     "lname": data['lname'],
     "address": data['address'],
     "branch": data['branch'],
     "course": '002',
     "email": data['email'],
     "phone": data['phone'],
     "password": data['phone'],
     "role": 'Faculty',
     "profile_pic":'https://static.vecteezy.com/system/resources/thumbnails/009/734/564/small/default-avatar-profile-icon-of-social-media-user-vector.jpg',
     
  }
  result = collection.insert_one(data_to_insert)
  return redirect('/Subadmin-faculty/')



def addfaculty_edit_GET(request):
  collection = db["users"]
  results = collection.find({'_id':ObjectId(request.GET['id'])})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document
  branch=getbranch()
  return render(request,f'{uname}/edit-faculty.html',{'title':'faculty','data':data,'branch':branch})


def addfaculty_edit_POST(request):
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
  return redirect('/Subadmin-faculty/')


def addfaculty_delete_POST(request):
  collection = db["users"]
  result = collection.delete_one({"_id":ObjectId(request.GET['id'])})
  print("Deleted Count:", result.deleted_count)
  return redirect('/Subadmin-faculty/')


