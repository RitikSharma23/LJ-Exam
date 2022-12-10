from django.shortcuts import render,HttpResponse
from adminpage.models import *
from openpyxl import Workbook
import openpyxl
import mysql.connector
import json
import ast

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="python"
)
mycursor = mydb.cursor()

def markshome(request):
    d=Subject.objects.all().values()
    details={'subjectlist':d}
    return render(request,"marks.html",details)

def adminpage(request):
    return render(request,"admin.html",{})

def marksoption(request):
    data=request.POST
    d=Subject.objects.filter(subjectcode=data['subjectcode']).values()
    details={'subject':d[0],'year':data['year']}
    return render(request,"marksoption.html",details)


def theory(request):
    data=request.POST
    d=Subject.objects.filter(subjectcode=data['subjectcode']).values()
    g=Grade.objects.all().values()
    details={
        'subject':d[0],'year':data['year'],'type':data['type'],'grade':g
    }
    return render(request,"theory.html",details)


def uploadtheory(request):

    if "GET" == request.method:
        return render(request, 'myapp/index.html', {})
    else:
        data=request.POST
        excel_file = request.FILES["theoryexcel"]
        d=Subject.objects.filter(subjectcode=data['subjectcode']).values()
        g=Grade.objects.all().values()
        wb = openpyxl.load_workbook(excel_file)

        worksheet = wb["Students Seat"]
        excel_data = list()

        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
        passing=g[len(g)-1]['r2']

        detail={'excel':excel_data,'subject':d[0],'grade':g,'year':data['year'],'passing':passing}

        return render(request,"theoryexcel.html",detail)


def submittheory(request):
    data=request.POST
    data=dict(data)

    d=Subject.objects.filter(subjectcode=data['subjectcode'][0]).values()
    d=d[0]
    sub=str(d['sem'])+"_"+d['subjectcode']+"_t"
    
    
    marks={}
    for d in range(0,len(data['enrollment'])):
        mycursor.execute("SELECT "+sub+" FROM adminpage_studentmarks WHERE enrollment='"+data['enrollment'][d]+"'")
        myresult = mycursor.fetchall()

        if(myresult[0][0]=="n"):
            marks={
                'Status':data['status'][d],
                'Grade':data['grade'][d],
                'year':{
                    str(data['year'][0]):{data['type'][0]:{'marks':data['marks'][d],'out':data['total'][0],'grade':data['grade'][d], 'credit':data['gradepoint'][d]},
                    },
                }
            }
            res = json.dumps(marks)

            c=("INSERT INTO adminpage_studentmarks ("+sub+") VALUES('"+str(marks)+"') WHERE enrollment='"+data['enrollment'][d]+"'")
            c="UPDATE `adminpage_studentmarks` SET `"+sub+"` = '"+res+"' WHERE `adminpage_studentmarks`.`enrollment` = '"+data['enrollment'][d]+"';"
            mycursor.execute(c)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")

        else:
            marks = ast.literal_eval(myresult[0][0])
            print(marks)
            marks['Status']=data['status'][d]
            marks['Grade']=data['grade'][d]

            add={'marks':data['marks'][d],'out':data['total'][0],'grade':data['grade'][d], 'credit':data['gradepoint'][d]}
            
            marks['year'][data['year'][0]]=add
            
            res = json.dumps(marks)

            c=("INSERT INTO adminpage_studentmarks ("+sub+") VALUES('"+str(marks)+"') WHERE enrollment='"+data['enrollment'][d]+"'")
            c="UPDATE `adminpage_studentmarks` SET `"+sub+"` = '"+res+"' WHERE `adminpage_studentmarks`.`enrollment` = '"+data['enrollment'][d]+"';"
            mycursor.execute(c)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
 
    


    return HttpResponse("<pre>"+str(marks)+"</pre>")