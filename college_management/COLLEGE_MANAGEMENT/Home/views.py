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
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage

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
  password = "@"
  receiver_email =data['email']
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

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse

def upload_file(request):
  file_uploaded = request.FILES['file_uploaded']
  fs = FileSystemStorage()
  filename = fs.save(file_uploaded.name, file_uploaded)
  file_url = fs.url(filename)
  return JsonResponse({'message': 'File uploaded and saved successfully', 'filename': filename, 'file_url': file_url})


def testpage(request):
  return render(request,'test.html',{})


# Add This To Your URLS.py File
# path('generate_pdf/', generate_pdf, name='generate_pdf'),


# Views.py Function

from django.http import FileResponse
from django.shortcuts import render
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from io import BytesIO

def generate_pdf(request):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    
    # Fetch Data From Your Database

    data = [
        ["Name", "Roll"],
        ["Ritik Sharma", 62],
        ["Shanu Pandey", 29,],
        ["Vrutik Jagad", 18,],
    ]

    table_data = []
    for row in data:
        table_data.append(row)

    table = Table(table_data)
    
    # Add More Styles According To Your Needs
    style = TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
        # ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        # ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        # ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        # ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        # ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        # ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])

    table.setStyle(style)
    elements.append(table)
    doc.build(elements)
    buffer.seek(0)
    response = FileResponse(buffer, as_attachment=True, filename='sample_table.pdf')
    return response




