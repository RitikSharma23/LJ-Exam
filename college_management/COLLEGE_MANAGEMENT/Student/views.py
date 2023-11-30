
from django.shortcuts import render,redirect
import pymongo
import json
from bson import json_util
from bson import ObjectId
from django.contrib.sessions.models import Session
import pandas as pd
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.



mongo_uri = "mongodb+srv://ljexam:LjExam@ljexam.vysc2ku.mongodb.net/"

client = pymongo.MongoClient(mongo_uri)

database_name = "LJKU"
db = client[database_name]

uname='Student'
# Create your views here.


def dashboard(request):
  return render(request,f'{uname}/dashboard.html',{'title':'Dashboard'})


def profile(request):
  collection = db["users"]
  results = collection.find({'email':request.session.get("email")})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document
  return render(request,f'{uname}/profile.html',{'title':'profile','data':data})