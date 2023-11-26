
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
  results = collection.find({'role': 'Faculty'})
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

