from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from adminpage.models import *
from django.contrib import messages
import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="python"
)
mycursor = mydb.cursor()


# Create your views here.

def adminpage(request):
    mycursor.execute("SELECT Institute_Code FROM course")
    institute = mycursor.fetchall()
    details={'institute':institute}
    return render(request,"admin.html",details)

def addinstitute(request):
    return render(request,"addinstitute.html",{})

def doaddinstitute(request):
    data=request.POST
    print(data)
    val=data['institute_code'],data['institute_name'],data['program_code'],data['degree_name'],data['program_type'],data['program_category'],data['branch_name']

    sql = "INSERT INTO course (institute_code,institute_name,program_code,degree_name,type,category,branch) VALUES (%s,%s,%s,%s,%s,%s,%s)"

    mycursor.execute(sql, val)
    x=mycursor.rowcount
    mydb.commit()

    messages.success(request,"Added Successfully")
    print(data['institute_code'])
    return render(request,"addinstitute.html",{})
    