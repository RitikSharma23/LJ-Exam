from django.shortcuts import render,HttpResponse
from adminpage.models import *
from adminpage.views import *
from adminpage.templates import *

def resulthome(request):
    data={}
    print(institute)
    print(program)
    return selectcourse(request,"resulthome.html",data)

def viewresult(request):
    data=request.POST
    global institute,program
    mydb=mysql.connector.connect(**config)
    mycursor = mydb.cursor()
    c=("SELECT DISTINCT SUBSTRING(enrollment, 1, 2) AS batch,sem as sem FROM adminpage_studentdetails WHERE institute_code='"+str(data['institute'])+"' and program_code='"+str(data['program'])+"';")
    mycursor.execute(c)
    myresult = mycursor.fetchall()
    mydb.close()
    print(c)

    data={'batchlist':myresult}
    return selectcourse(request,"viewresult.html",data)
