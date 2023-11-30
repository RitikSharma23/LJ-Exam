
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

uname='Faculty'


def dashboard(request):
  return render(request,f'{uname}/dashboard.html',{'title':'Dashboard'})


def profile(request):
  return render(request,f'{uname}/profile.html',{'title':'profile'})


def profile_edit_GET(request):
  
  return render(request,f'{uname}/edit-profile.html',{'title':'edit-profile'})


def marksentry(request):
  collection = db["exams"]
  results = collection.find({'assigned_to':request.session.get("email")})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[str(document['_id'])]=document
  return render(request,f'{uname}/marksentry.html',{'title':'marksentry','data':data})

def entermarks_GET(request):
  collection = db["exams"]
  results = collection.find({'_id':ObjectId(request.POST['id'])})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[str(document['_id'])]=document
  return render(request,f'{uname}/enter-marks.html',{'title':'marksentry','data':data[request.POST['id']]})


def generateseat(request):
  return render(request,f'{uname}/generateseat.html',{'title':'generateseat'})


from django.http import Http404

def update_marks(request, document_id):
    print(f"Received document_id: {document_id}")
    if request.method == 'POST':
        marks_data = request.POST.getlist('marks')
        print(marks_data)


        collection = db['exams']
        document = collection.find_one({'_id': ObjectId(document_id)})
        for enrollment, marks in zip(document['student_data'].keys(), marks_data):
            query = {'_id': ObjectId(document_id), f'student_data.{enrollment}.marks': {'$ne': marks}}
            update = {'$set': {f'student_data.{enrollment}.marks': int(marks)}}
            collection.update_one(query, update)

    return redirect(f'/{uname}-marksentry/')



