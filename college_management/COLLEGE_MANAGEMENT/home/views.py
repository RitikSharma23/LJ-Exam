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

def home(request):
  return render(request, 'home.html',{})

def login(request):
  return render(request, 'login.html',{})

def logout(request):
  request.session.clear()
  request.session['is_authenticated'] = False
  return redirect("/")

def postLogin(request):
    print("POST LOGIN")
    data = request.POST
    collection = db["users"]
    criteria1 = {"email": data['email']}
    criteria2 = {"password": data['password']}

    query = {"$and": [criteria1, criteria2]}
    try:
        result = collection.find(query)
        
   
        request.session['fname'] = result[0]['fname']
        request.session['lname'] = result[0]['lname']
        request.session['profile_pic'] = result[0]['profile_pic']
        request.session['email'] = result[0]['email']
        request.session['role'] = result[0]['role']
        request.session['branch'] = result[0]['branch']
        request.session['is_authenticated'] = True
        request.session.save()
        
        return redirect(f"/{result[0]['role']}-dashboard/")
          
    except Exception as e:
        print(e)
        messages.error(request, 'Invalid Email And Password')
        return redirect('/login/')
