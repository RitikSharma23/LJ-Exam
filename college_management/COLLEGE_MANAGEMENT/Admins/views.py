from django.shortcuts import render,redirect
import pymongo
import json
from bson import json_util
from bson import ObjectId
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


mongo_uri = "mongodb+srv://ljexam:LjExam@ljexam.vysc2ku.mongodb.net/"

client = pymongo.MongoClient(mongo_uri)

database_name = "LJKU"
db = client[database_name]

uname='Admins'

def getbranch(branch):
  collection = db["course"]
  results = collection.find({'branch':branch})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[str(document['_id'])]=document
  return data
  


def dashboard(request):
  return render(request,f'{uname}/dashboard.html',{'title':'Dashboard'})

def subadmins(request):
  collection = db["users"]
  results = collection.find({'role': 'Subadmin'})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[str(document['_id'])]=document
  return render(request,f'{uname}/subadmins.html',{'title':'Subadmins','data':data})

def subadmins_GET(request):
  branch=getbranch(request.session.get("branch"))
  return render(request,f'{uname}/add-subadmins.html',{'title':'Subadmins','branch':branch})

def subadmins_POST(request):
  data=(request.POST)
  collection = db["users"]
  data_to_insert = {
     "fname": data['fname'],
     "lname": data['lname'],
     "address": data['address'],
     "branch": request.session.get("branch"),
     "email": data['email'],
     "course": data['course'],
     "phone": data['phone'],
     "password": data['phone'],
     "role": 'Subadmin',
     "profile_pic":'https://static.vecteezy.com/system/resources/thumbnails/009/734/564/small/default-avatar-profile-icon-of-social-media-user-vector.jpg',
     
  }
  result = collection.insert_one(data_to_insert)
  return redirect(f'/{uname}-subadmins/')

def subadmins_edit_GET(request):
  collection = db["users"]
  results = collection.find({'_id':ObjectId(request.GET['id'])})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document
  branch=getbranch(request.session.get("branch"))
  return render(request,f'{uname}/edit-subadmins.html',{'title':'edit subadmins','data':data,'branch':branch})


def subadmins_edit_POST(request):
  data=(request.POST)
  collection = db["users"]
  data_to_insert = {"$set":{
     "fname": data['fname'],
     "lname": data['lname'],
     "address": data['address'],
     "branch": request.session.get("branch"),
     "email": data['email'],
     "course": data['course'],
     "phone": data['phone'],
     "password": data['phone'],
  }}
  result = collection.update_one({"_id":ObjectId(request.POST['id'])}, data_to_insert) 
  return redirect(f'/{uname}-subadmins/')



def subadmins_delete_POST(request):
  collection = db["users"]
  result = collection.delete_one({"_id":ObjectId(request.GET['id'])})
  print("Deleted Count:", result.deleted_count)
  return redirect(f'/{uname}-subadmins/')



def calendar(request):
  return render(request,f'{uname}/calendar.html',{'title':'calendar'})

def email(request):
  return render(request,f'{uname}/email.html',{'title':'email'})








def subjects(request):
  collection = db["subjects"]
  results = collection.find()
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[str(document['_id'])]=document
  return render(request,f'{uname}/subjects.html',{'title':'subjects','data':data})

def subjects_GET(request):
  branch=getbranch(request.session.get("branch"))
  return render(request,f'{uname}/add-subjects.html',{'title':'subjects','branch':branch})

def subjects_POST(request):
  data=(request.POST)
  collection = db["subjects"]
  data_to_insert = {
     "name": data['name'],
     "code": data['code'],
     "branch": request.session.get("branch"),
     "course": data['course'],
     "is_mark": False,
     "is_theory": False,
     "is_practical": False,
     "is_mid": False,
     "theory_total": 0,
     "practical_total": 0,
     "mid_total": 0,
     "theory_pass": 0,
     "practical_pass": 0,
     "mid_pass": 0,
     "sem": data['sem'],
  }
  result = collection.insert_one(data_to_insert)
  return redirect('/Admins-subjects/')

def subjects_edit_GET(request):
  collection = db["subjects"]
  results = collection.find({'_id':ObjectId(request.GET['id'])})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document
  branch=getbranch(request.session.get("branch"))

  return render(request,f'{uname}/edit-subjects.html',{'title':'subjects','data':data,'branch':branch})


def subjects_edit_POST(request):
  data=(request.POST)
  collection = db["subjects"]
  data_to_insert = {"$set":{
     "name": data['name'],
     "code": data['code'],
     "course": data['course'],
     "sem": data['sem'],
  }}
  result = collection.update_one({"_id":ObjectId(request.POST['id'])}, data_to_insert) 
  return redirect('/Admins-subjects/')


def subjects_delete_POST(request):
  collection = db["subjects"]
  result = collection.delete_one({"_id":ObjectId(request.GET['id'])})
  print("Deleted Count:", result.deleted_count)
  return redirect('/Admins-subjects/')







def marks(request):
  collection = db["subjects"]
  results = collection.find()
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[str(document['_id'])]=document
  return render(request,f'{uname}/marks.html',{'title':'marks','data':data})

def marks_GET(request):
  collection = db["subjects"]
  results = collection.find({'_id':ObjectId(request.GET['id'])})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document
  print(data)

  # return render(request,f'{uname}/edit-exam.html',{'title':'exam'})
  return render(request,f'{uname}/add-marks.html',{'title':'marks','data':data})

@csrf_exempt
def marks_POST(request):
  data = json.loads(request.body.decode('utf-8'))
  collection = db["subjects"]
  data_to_insert = {"$set":{
     "is_mark": True,
     "is_theory":data['is_theory'],
     "is_practical":data['is_practical'],
     "is_mid":data['is_mid'],
     "theory_total":data['theory_total'],
     "practical_total":data['practical_total'],
     "mid_total":data['mid_total'],
     "theory_pass":data['theory_pass'],
     "practical_pass":data['practical_pass'],
     "mid_pass":data['mid_pass'],
  }}
  result = collection.update_one({"_id":ObjectId(data['id'])}, data_to_insert) 
 
  return JsonResponse({'status': True})

def marks_edit_GET(request):
  collection = db["marks"]
  results = collection.find({'_id':ObjectId(request.GET['id'])})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document

  return render(request,f'{uname}/edit-marks.html',{'title':'marks','data':data})


def marks_edit_POST(request):
  data=(request.POST)
  collection = db["marks"]
  data_to_insert = {"$set":{
     "code": data['code'],
     "name": data['name'],
     "email": data['email'],
     "phone": data['phone'],
     "address": data['address'],
  }}
  result = collection.update_one({"_id":ObjectId(request.POST['id'])}, data_to_insert) 
  return redirect('/Admins-marks/')


def marks_delete_POST(request):
  collection = db["marks"]
  result = collection.delete_one({"_id":ObjectId(request.GET['id'])})
  print("Deleted Count:", result.deleted_count)
  return redirect('/Admins-marks/')











def exam(request):
  collection = db["exam"]
  results = collection.find()
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[str(document['_id'])]=document
  return render(request,f'{uname}/exam.html',{'title':'exam','data':data})

def exam_GET(request):
  return render(request,f'{uname}/add-exam.html',{'title':'exam'})

def exam_POST(request):
  data=(request.POST)
  collection = db["exam"]
  data_to_insert = {
     "code": data['code'],
     "name": data['name'],
     "email": data['email'],
     "phone": data['phone'],
     "address": data['address'],
  }
  result = collection.insert_one(data_to_insert)
  return redirect('/Admins-exam/')

def exam_edit_GET(request):
  collection = db["exam"]
  results = collection.find({'_id':ObjectId(request.GET['id'])})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document

  return render(request,f'{uname}/edit-exam.html',{'title':'exam','data':data})


def exam_edit_POST(request):
  data=(request.POST)
  collection = db["exam"]
  data_to_insert = {"$set":{
     "code": data['code'],
     "name": data['name'],
     "email": data['email'],
     "phone": data['phone'],
     "address": data['address'],
  }}
  result = collection.update_one({"_id":ObjectId(request.POST['id'])}, data_to_insert) 
  return redirect('/Admins-exam/')


def exam_delete_POST(request):
  collection = db["exam"]
  result = collection.delete_one({"_id":ObjectId(request.GET['id'])})
  print("Deleted Count:", result.deleted_count)
  return redirect('/Admins-exam/')






 





def inbox(request):
  return render(request,f'{uname}/inbox.html',{'title':'inbox'})

def read(request):
  return render(request,f'{uname}/read.html',{'title':'read'})

def testform(request):
  print(request.POST)
  
  return render(request,f'{uname}/read.html',{'title':'read'})



def logout(request):
  print("admin logout")
  if request.session.get('is_authenticated', False):
    request.session.clear() 
    request.session['is_authenticated'] = True
    request.session.save()
     
  return redirect('/') 


