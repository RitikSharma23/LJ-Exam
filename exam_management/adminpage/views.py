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
    val=data['institute_code'],data['institute_name'],data['program_code'],data['degree_name'],data['program_type'],data['program_category'],data['branch_name']
    sql = "INSERT INTO course (institute_code,institute_name,program_code,degree_name,type,category,branch) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,val)
    x=mycursor.rowcount
    mydb.commit()
    if(x==1):
         return HttpResponse('{"status":"success"}')
    else: return HttpResponse('{"status":"fail"}')

def findinstitute(request):return render(request,"findinstitute.html",{})

def editinstitute(request):
    data=request.POST
    mycursor.execute("SELECT * FROM course where institute_code='"+data['institute_code']+"' and program_code='"+data['program_code']+"'")
    myresult = mycursor.fetchall()
    if len(myresult)==1:
        data={
        "id":myresult[0][0],
        "institute_code":myresult[0][1],
        "program_code":myresult[0][2],
        "program_type":myresult[0][3],
        "institute_name":myresult[0][4],
        "degree_name":myresult[0][5],
        "program_category":myresult[0][6],
        "branch_name":myresult[0][7],
        }
        return render(request,"editinstitute.html",data)
    else:
        return HttpResponse("NO Data Found")


def doeditinstitute(request):
    data=request.POST
    val=data['institute_code'],data['institute_name'],data['program_code'],data['degree_name'],data['program_type'],data['program_category'],data['branch_name'],data['uid']
    sql = "UPDATE course set institute_code=%s,institute_name=%s,program_code=%s,degree_name=%s,type=%s,category=%s,branch=%s where id=%s"
    print(val)
    mycursor.execute(sql,val)
    x=mycursor.rowcount
    mydb.commit()
    if(x==1):
         return HttpResponse('{"status":"success"}')
    else: return HttpResponse('{"status":"fail"}')


    