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

