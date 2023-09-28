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


def check_session(request):
    if not request.session.get('authenticated', False):
        return redirect('login')


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
   
        request.session['email'] = result[0]['email']
        request.session['role'] = result[0]['role']
        request.session['is_authenticated'] = True
        
        if result[0]['role'] == 'Superadmin':
            return redirect('/superadmin/dashboard/')
        elif result[0]['role'] == 'Subadmin':
            return redirect('/subadmin/dashboard/')
        elif result[0]['role'] == 'Admin':
            return redirect('/admins/dashboard/')
          
    except Exception as e:
        print(e)
        messages.error(request, 'Invalid Email And Password')
        return redirect('/login/')
