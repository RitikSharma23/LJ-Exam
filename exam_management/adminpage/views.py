from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from adminpage.models import *
from django.contrib import messages
import mysql.connector


institute=""
program=""

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="python"
)
mycursor = mydb.cursor()



def clear(request):
    global institute,program
    institute=""
    program=""
    return HttpResponse("cleared")

def addcourse(request):
    global institute,program
    data=request.POST
    institute=data['institute_code']
    program=data['program_code']
    return HttpResponse(data['institute_code'])

def selectcourse(request,page,data):
    global institute,program    

    if(institute==""):
        mycursor.execute("SELECT Institute_Code FROM course")
        inst = mycursor.fetchall()
        details={'institute':[*set(inst)],'pro':False,'ins':True}
        return render(request,"selectcourse.html",details)
    elif(program==""):
        mycursor.execute("SELECT program_Code FROM course where Institute_Code='"+institute+"'")
        inst = mycursor.fetchall()
        details={'institut':inst,'pro':True,'ins':False,'institute':institute}
        return render(request,"selectcourse.html",details)
    else:
        mycursor.execute("SELECT institute_Code,program_code,type,institute_Name,degree_Name,category,branch FROM course where Institute_Code='"+institute+"' and program_Code='"+program+"'")
        c=mycursor.fetchall()
        for i in c:
            c=i
        data['course']=c
        return render(request,page,data)

def adminpage(request):  
    data={}
    return selectcourse(request,"admin.html",data)

def addinstitute(request):
    data={}
    return selectcourse(request,"addinstitute.html",data)

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

def findinstitute(request):    
    data={}
    return selectcourse(request,"findinstitute.html",data)

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
        return selectcourse(request,"editinstitute.html",data)
    else:
        return HttpResponse("NO Data Found")


def doeditinstitute(request):
    data=request.POST
    val=data['institute_code'],data['institute_name'],data['program_code'],data['degree_name'],data['program_type'],data['program_category'],data['branch_name'],data['uid']
    sql = "UPDATE course set institute_code=%s,institute_name=%s,program_code=%s,degree_name=%s,type=%s,category=%s,branch=%s where id=%s"
    mycursor.execute(sql,val)
    x=mycursor.rowcount
    mydb.commit()
    if(x==1):
         return HttpResponse('{"status":"success"}')
    else: return HttpResponse('{"status":"fail"}')


def addstudent(request):
    data={}
    return selectcourse(request,"addstudent.html",data)

def doaddstudent(request):
    data=request.POST

    val=data['enrollment'],data['sem'],data['roll'],data['oldenrollment'],data['name'],data['phone'],data['email'],data['gender'],data['dob'],data['caste'],data['subcast'],data['category'],data['photo'],data['institute_code'],data['program_code'],data['parent_contact'],data['emergency_contact'],data['userid'],data['address'],data['aadhaar'],data['finalsem'],data['term_end'],data['total_credits'],data['total_grade_points'],data['total_backlog']   
    sql = "INSERT INTO student_details (enrollment,sem,roll,oldenrollment,name,phone,email,gender,dob,caste,subcast,category,photo,institute_code,program_code,parent_contact,emergency_contact,userid,address,aadhaar,finalsem,term_end,total_credits,total_grade_points,total_backlog)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,val)
    mydb.commit()

    sql1 = "INSERT INTO student_marks (enrollment) VALUES ('"+data['enrollment']+"')"
    mycursor.execute(sql1)
    mydb.commit()
    x=mycursor.rowcount
    
    if(x==1):
         return HttpResponse('{"status":"success"}')
    else: return HttpResponse('{"status":"fail"}')





    