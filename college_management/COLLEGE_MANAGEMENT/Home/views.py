from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
import pymongo
import json
from bson import json_util
from bson import ObjectId
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader

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
    
    print(criteria1)
    print(criteria2)

    query = {"$and": [criteria1, criteria2]}
    try:
        result = collection.find(query)
   
        request.session['fname'] = result[0]['fname']
        request.session['lname'] = result[0]['lname']
        request.session['profile_pic'] = result[0]['profile_pic']
        request.session['email'] = result[0]['email']
        request.session['role'] = result[0]['role']
        request.session['branch'] = result[0]['branch']
        request.session['course'] = result[0]['course']
        request.session['is_authenticated'] = True
        request.session.save()
        
        if(result[0]['role']=='Admin'):
          print("REDIRECTED TO ADMIN")
          return redirect(f"/{result[0]['role']}s-dashboard/")
        else:
          return redirect(f"/{result[0]['role']}-dashboard/")
          
    except Exception as e:
        print(e)
        messages.error(request, 'Invalid Email And Password')
        return redirect('/login/')
      



def passpage(request):
  return render(request,'forgot.html',{})


def postforgot(request):
  print(request.POST)
  passmail(request.POST['email'])
  messages.success(request, 'Email Sent Successfully')
  return render(request,'forgot.html',{})


def postreset(request):
  try:
      data=(request.POST)
      collection = db["users"]
      data_to_insert = {"$set":{
        "password": data['password'],
      }}
      result = collection.update_one({"_id":ObjectId(request.POST['uid'])}, data_to_insert) 

      collection = db["temp"]
      result = collection.delete_one({"_id":ObjectId(request.POST['tid'])})
      print("Deleted Count:", result.deleted_count)
  
      return redirect('/')
  except:
    return HttpResponse("Link Expired")




def passwordReset(request):
  try:
    collection = db["temp"]
    results = collection.find({'_id':ObjectId(request.GET['id'])})
    data={}
    for document in results:
      document['id']=str()
      data=document
    
    collection = db["users"]
    results = collection.find({'_id':ObjectId(data['uid'])})
    data={}
    for document in results:
      document['id']=str(document['_id'])
      data=document
    return render(request,'password.html',{'data':data,'tid':request.GET['id']})
  except Exception as e:
    return HttpResponse("Link Expired")



from django.conf import settings
import os


def passmail(email):
  
  tp = os.path.join(settings.BASE_DIR, 'email.html')
  
  collection = db["users"]
  results = collection.find({'email':email})
  data={}
  for document in results:
    document['id']=str(document['_id'])
    data=document
  
  collection = db['temp']
  collection.create_index([("expire_at", pymongo.ASCENDING)], expireAfterSeconds=300)

  new_id = ObjectId()

  document = {
      "_id": new_id,
      "uid": data['id'],
      'status': True,
      "expire_at": datetime.utcnow() + timedelta(seconds=300)
  }  
  collection.insert_one(document)


  sender_email = "ritik.sharma@techglide.in"
  receiver_email =data['email']
  password = "Dcba4321@"
  subject = "Reset Your Password"

  template_path =tp

  with open(template_path, "r") as template_file:
      html_template = template_file.read()    

  variables = {
      "fname": data['fname'],
      "lname": data['lname'],
      "id": "http://127.0.0.1:8000/reset-password?id="+str(new_id)
  }

  for key, value in variables.items():
      html_template = html_template.replace("{{" + key + "}}", str(value))

  msg = MIMEMultipart()
  msg["From"] = sender_email
  msg["To"] = receiver_email
  msg["Subject"] = subject

  msg.attach(MIMEText(html_template, "html"))

  smtp_server = "smtp.gmail.com"
  smtp_port = 587

  try:
      server = smtplib.SMTP(smtp_server, smtp_port)
      server.starttls()
      server.login(sender_email, password)

      server.sendmail(sender_email, receiver_email, msg.as_string())
      print("Email sent successfully")
  except Exception as e:
      print(f"Error: {str(e)}")

  finally:
      server.quit()

# passmail('ritikss748@gmail.com')