
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

uname='Subadmin'


def dashboard(request):
  return render(request,f'{uname}/dashboard.html',{'title':'Dashboard'})



def profile(request):
  return render(request,f'{uname}/profile.html',{'title':'profile'})


def profile_edit_GET(request):
  
  return render(request,f'{uname}/edit-profile.html',{'title':'edit-profile'})


def getbranch():
  collection = db["branch"]
  results = collection.find()
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[str(document['_id'])]=document
  return data



def faculty(request):
  collection = db["users"]
  results = collection.find({'role': 'Faculty'})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[str(document['_id'])]=document
  return render(request,f'{uname}/faculty.html',{'title':'faculty','data':data})

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
  return redirect(f'/{uname}-faculty/')



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
  return redirect(f'/{uname}-faculty/')


def addfaculty_delete_POST(request):
  collection = db["users"]
  result = collection.delete_one({"_id":ObjectId(request.GET['id'])})
  print("Deleted Count:", result.deleted_count)
  return redirect(f'/{uname}-faculty/')













def student(request):
  collection = db["students"]
  results = collection.find({'branch':int(request.session.get("branch")),'course':int(request.session.get("course"))})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[str(document['_id'])]=document
  return render(request,f'{uname}/student.html',{'title':'faculty','data':data})

def addstudent_GET(request):
  pass

def addstudent_POST(request):
  pass

def addstudent_edit_GET(request):
  pass

def addstudent_edit_POST(request):
  pass

def addstudent_delete_POST(request):
  pass

def upload_file(request):
    if request.method == 'POST' and request.FILES['file_uploaded']:
        file_uploaded = request.FILES['file_uploaded']
        if not file_uploaded.name.endswith('.csv'):
            return JsonResponse({'error': 'Only CSV files are allowed'})
        with open('temp_file.csv', 'wb+') as destination:
            for chunk in file_uploaded.chunks():
                destination.write(chunk)
        try:
            columns_to_read = ['fname','lname','email','gender','aadhar','phone','div']
            df = pd.read_csv('temp_file.csv', usecols=columns_to_read)
            missing_columns = set(columns_to_read) - set(df.columns)
            if missing_columns:
                return JsonResponse({'error': f'Missing columns: {", ".join(missing_columns)}'})
            
            data_list = df.to_dict(orient='records')

            collection = db["students"]

            for i in range(len(data_list)):
              results = collection.find_one({'aadhar': data_list[i]['aadhar']})

              if results:
                data_list[i]['is']=True
              else:
                data_list[i]['is']=False
            print(data_list)

            collection = db["course"]
            results_c = collection.find({'branch':request.session.get("branch"),'code':request.session.get("course")})
            data_c={}
            for document in results_c:
              document['id']=str(document['_id'])
              data_c=document
            
            return render(request, f'{uname}/excel.html', {'title': 'excel', 'data': data_list,'course':data_c})
        except pd.errors.EmptyDataError:
            return JsonResponse({'error': 'The uploaded CSV file is empty'})
        except Exception as e:
            return JsonResponse({'error': f'Error processing the CSV file: {str(e)}'})
    else:
        return JsonResponse({'error': 'Invalid request'})

@csrf_exempt
def verify_aadhar(request):
  collection = db["students"]
  results = collection.find_one({'aadhar': request.GET['id']})
  if results:
    return JsonResponse({'status': True})
  else:
    return JsonResponse({'status': False}) 

@csrf_exempt
def verify_email(request):
  collection = db["students"]
  results = collection.find_one({'email': request.GET['id']})
  if results:
    return JsonResponse({'status': True})
  else:
    return JsonResponse({'status': False}) 


@csrf_exempt
def verify_enroll(request):
  collection = db["students"]
  results = collection.find_one({'enrollment': request.GET['id']})
  if results:
    return JsonResponse({'status': True})
  else:
    return JsonResponse({'status': False}) 

@csrf_exempt
def add_student_POST(request):
  data = json.loads(request.body.decode('utf-8'))
  print(data)
  try:
    collection = db["students"]
    data_to_insert ={
      'enrollment':data['enrollment'],
      'roll':data['roll'],
      'fname':data['fname'],
      'lname':data['lname'],
      'div':data['div'],
      'email':data['email'],
      'gender':data['gender'],
      'aadhar':data['aadhar'],
      'phone':data['phone'],
      'start_year':data['start_year'],
      'end_year':data['end_year'],
      'branch':data['branch'],
      'total_year':data['total_year'],
      'course':data['course'],
      'total_sem':data['total_sem'],
    }
    result = collection.insert_one(data_to_insert) 
    print(result)
    return JsonResponse({'status': True})
  except:
    return JsonResponse({'status': False})




















def exam(request):
  collection = db["exams"]
  results = collection.find()
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data[str(document['_id'])]=document
    
  return render(request,f'{uname}/exam.html',{'title':'exam','data':data})

def addexam_GET(request):
    collection = db["subjects"]
    results = collection.find()
    sems = set()

    for document in results:
        sem_value = document.get('sem')
        if sem_value:
            sems.add(sem_value)

    return render(request, f'{uname}/add-exam.html', {'title': 'exam', 'branch': list(sems)})


def selectexam_GET(request):
    collection = db["students"]
    results = collection.find()
    batch = set()

    for document in results:
        sem_value = document.get('start_year')
        if sem_value:
            batch.add(sem_value)
    print(batch)
    return render(request, f'{uname}/select-exam.html', {'title': 'exam', 'branch': list(batch),'sem':request.POST['sem']})

def selectsubject_GET(request):
    collection = db["subjects"]
    results = collection.find({'branch':request.session.get("branch"),'course':request.session.get("course")})
    batch = set()
    return render(request, f'{uname}/select-subject.html', {'title': 'exam', 'subject': results,'sem':request.POST['sem'],'batch':request.POST['batch'],'type':request.POST['type'],'season':request.POST['season']})

from datetime import datetime
@csrf_exempt
def insert_exam_POST(request):
  data = json.loads(request.body.decode('utf-8'))

  collection = db["students"]
  results = collection.find({'branch': int(request.session.get("branch")),
                              'course': int(request.session.get("course")),
                              'start_year': int(data['batch'])})
  stdata = {}

  for document in results:
      subjects_list = list(data['subjects'])  # Convert subjects to a list

      for i in subjects_list:
          print("first Time", i['type'])

          d = {}
          document['id'] = str(document['_id'])
          d['enrollment'] = document['enrollment']
          d['fname'] = document['fname']
          d['div'] = document['div']
          d['branch'] = str(document['branch']).zfill(3)
          d['course'] = str(document['course']).zfill(3)
          d['seat'] = (
              data['season'] + (datetime.now().strftime("%Y")[-2:]) +
              str(document['total_year']) + d['course'] +
              str(document['roll']).zfill(3)
          )
          d['subject'] = i['code']
          d['name'] = i['name']
          d['type'] = i['type']
          d['date'] = str(datetime.strptime(i['date'], "%Y-%m-%dT%H:%M").date())
          d['time'] = str(datetime.strptime(i['date'], "%Y-%m-%dT%H:%M").time())
          d['price'] = i['price']
          d['is_paid'] = False
          d['marks'] = 0
          d['is_pass'] = False
          stdata[document['enrollment'] + i['type']] = d

  
  collection = db["exams"]
  data_to_insert = {
     "is_approved":False,
     "is_marks":False,
     "is_assigned":False,
     "assigned_to":"",
     "is_completed":False,
     'branch': request.session.get("branch"),
     'course': request.session.get("course"),
     "batch":data['batch'],
     "type":data['type'],
     "season":data['season'],
     "student_data":stdata
  }
  result = collection.insert_one(data_to_insert)
  
  try:
    return JsonResponse({'status': True})
  except:
    return JsonResponse({'status': False})











def addexam_POST(request):
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
     "role": 'exam',
     "profile_pic":'https://static.vecteezy.com/system/resources/thumbnails/009/734/564/small/default-avatar-profile-icon-of-social-media-user-vector.jpg',
  }
  result = collection.insert_one(data_to_insert)
  return redirect(f'/{uname}-exam/')



def addexam_edit_GET(request):
  collection = db["users"]
  results = collection.find({'_id':ObjectId(request.GET['id'])})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document
  branch=getbranch()
  return render(request,f'{uname}/edit-exam.html',{'title':'exam','data':data,'branch':branch})


def addexam_edit_POST(request):
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
  return redirect(f'/{uname}-exam/')


def addexam_delete_POST(request):
  collection = db["users"]
  result = collection.delete_one({"_id":ObjectId(request.GET['id'])})
  print("Deleted Count:", result.deleted_count)
  return redirect(f'/{uname}-exam/')



def viewexam_edit_GET(request):
  collection = db["exams"]
  results = collection.find({'_id':ObjectId(request.GET['id'])})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document
  
  collection = db["users"]
  results = collection.find({'role': 'Faculty'})
  data1={}
  for document in results:
    document['id']=str(document['_id'])
    data1[str(document['_id'])]=document
  return render(request,f'{uname}/view-exam.html',{'title':'exam','data':data,'faculty':data1})


def closeexam_edit_GET(request):
  data=(request.POST)
  collection = db["exams"]
  data_to_insert = {"$set":{
     "is_completed": True,
  }}
  result = collection.update_one({"_id":ObjectId(request.POST['id'])}, data_to_insert) 
  return redirect(f'/{uname}-exam/')

def assignexam_edit_GET(request):
  data=(request.POST)
  collection = db["exams"]
  data_to_insert = {"$set":{
     "is_assigned": True,
     "assigned_to":data['faculty']
  }}
  result = collection.update_one({"_id":ObjectId(request.POST['id'])}, data_to_insert) 
  return redirect(f'/{uname}-exam/')

