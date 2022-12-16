from django.shortcuts import render,HttpResponse
from adminpage.models import *
from adminpage.views import *
from adminpage.templates import *
import ast

def resulthome(request):
    data={}
    return selectcourse(request,"resulthome.html",data)

def viewresult(request):
    data=request.POST
    mydb=mysql.connector.connect(**config)
    mycursor = mydb.cursor()
    c=("SELECT DISTINCT SUBSTRING(enrollment, 1, 2) AS batch,sem as sem FROM adminpage_studentdetails WHERE institute_code='"+str(data['institute'])+"' and program_code='"+str(data['program'])+"';")
    mycursor.execute(c)
    myresult = mycursor.fetchall()
    mydb.close()

    data={'batchlist':myresult}
    return selectcourse(request,"viewresult.html",data)


def find(request):
    data=request.POST
    d=Subject.objects.filter(sem=1,institute_code='004',program_code='002').values()

    query=""
    theory=list()
    practical=list()
    mid=list()


    mydb=mysql.connector.connect(**config)
    mycursor = mydb.cursor()    
    subject=dict()

    co=("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'adminpage_studentmarks' AND COLUMN_NAME LIKE '1_%';")
    mycursor.execute(co)
    column = mycursor.fetchall()

    for c in column:
        print(c[0])
    
    

    return HttpResponse("hii")