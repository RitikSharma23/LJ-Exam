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
    grade=Grade.objects.values().all()
    col=list()
    for a in d:
        r=""
        if(a['theory']):r=r+",1_"+(str(a['subjectcode'])+"_t")
        if(a['practical']):r=r+",1_"+(str(a['subjectcode'])+"_p")
        if(a['mid']):r=r+",1_"+(str(a['subjectcode'])+"_m")
        col.append(r)

    mydb=mysql.connector.connect(**config)
    mycursor = mydb.cursor()    

    res=list()
    for  q in col:
        co=("SELECT enrollment"+q+" FROM `adminpage_studentmarks` WHERE enrollment='21004500210001'")
        mycursor.execute(co)
        res.append(mycursor.fetchall())
    x=0

    marks=list()
    
    for i in res:
        temp=list()
        t = ast.literal_eval(i[0][1])

        temp.append(d[x]['subjectcode'])
        temp.append(d[x]['subjectname'])
        temp.append(d[x]['credit'])

        if "theory" in t['year']['2021'].keys():
            temp.append(str(t['year']['2021']['theory']['marks']))
            temp.append(str(t['year']['2021']['theory']['grade']))
        else:temp.append("-");temp.append("-")
        
        p = ast.literal_eval(i[0][2])

        if "practical" in p['year']['2021'].keys():
            temp.append(str(p['year']['2021']['practical']['marks']))
            temp.append(str(p['year']['2021']['practical']['grade']))
        else:temp.append("-");temp.append("-")

        if "theory" in t['year']['2021'].keys() and "practical" in p['year']['2021'].keys():
            avg=(float(t['year']['2021']['theory']['marks'])+float(p['year']['2021']['practical']['marks']))/2
        else:
            avg="-"
        
        temp.append(str(avg))

        if avg!="-":
            for g in grade:
                if(avg>=g['r1'] and avg<=(float(g['r2'])+0.99)):
                    temp.append(g['grade'])
        else:
             temp.append("-")

        x=x+1
        print(len(temp))
        marks.append(temp)

    print(marks)

    

    return HttpResponse("hii")