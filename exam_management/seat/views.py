from django.shortcuts import render,HttpResponse
from adminpage.models import *
import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="python"
)
mycursor = mydb.cursor()

# SELECT DISTINCT SUBSTRING(enrollment, 1, 2) AS ExtractString
# FROM adminpage_studentdetails;

# UPDATE adminpage_studentdetails set sem ='3' WHERE institute_code='004' and program_code='002' and enrollment like '21%';

def seathome(request):
    d=Subject.objects.all().values()
    details={'subjectlist':d}
    return render(request,"seat.html",details)

def seatoption(request):
    data=request.POST
    d=Subject.objects.filter(subjectcode=data['subjectcode']).values()
    # print(d)
    details={
        'data':data,
        'subject':d[0]
    }
    return render(request,"seatoption.html",details)

def remedial(request):1

def adminpage(request):
    return render(request,"admin.html",{})

# =================  seat ===================

def seatsem(request):
    data=request.POST
    d=Subject.objects.filter(subjectcode=data['subjectcode']).values()
    d=d[0]

    mycursor.execute("SELECT enrollment,name FROM adminpage_studentdetails WHERE enrollment like '__"+str(d['institute_code'])+"_"+str(d['program_code'])+"%' and sem="+str(d['sem'])+";")

    myresult = mycursor.fetchall()
 
    for i in myresult:
        print(data['session']+data['year'][2:]+data['subjectcode'][1:5]+str(d['sem'])+i[0][-3:])

    return HttpResponse('{"status":"success"}')