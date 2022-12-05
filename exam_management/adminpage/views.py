from django.shortcuts import render,HttpResponse,HttpResponseRedirect,HttpResponsePermanentRedirect
from adminpage.models import *
from django.urls import reverse
from django.contrib import messages
import openpyxl
from openpyxl import *
import mysql.connector
import os
from django.http import FileResponse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

institute=""
program=""

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="python"
)
mycursor = mydb.cursor()

fields=['enrollment','sem','roll','oldenrollment','name','phone','email','gender','dob','caste','subcast','category','password','photo','institute_code','program_code','parent_contact','emergency_contact','userid','address','aadhaar','finalsem','term_end','total_credits','total_grade_points','total_backlog']



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
    print(institute)
    return HttpResponse(data['institute_code'])

def selectcourse(request,page,data):
    global institute,program   
    db=Course.objects.values_list('institute_Code')
    if not db:
        return render(request,"addinstitute.html",{})
    else:
        if(Course.objects.values_list('institute_Code')):
            if(institute==""):
                mydata = Course.objects.values_list('institute_Code')
                details={'institute':[*set(mydata)],'pro':False,'ins':True}
                return render(request,"selectcourse.html",details)
            elif(program==""):
                mydata = Course.objects.values_list('program_code').filter(institute_Code=institute)
                details={'institut':mydata,'pro':True,'ins':False,'institute':institute}
                return render(request,"selectcourse.html",details)
            else:
                db=Course.objects.values_list('institute_Code','program_code','type','institute_Name','degree_Name','category','branch').filter(institute_Code=institute,program_code=program)
                data['course']=db[0]
                return render(request,page,data)

def adminpage(request):  
    data={}
    return selectcourse(request,"admin.html",data)

def addinstitute(request):
    data={}
    return selectcourse(request,"addinstitute.html",data)

def doaddinstitute(request):
    data=request.POST
    db=Course(institute_Code=data['institute_code'],program_code=data['program_code'],type=data['program_type'],institute_Name=data['institute_name'],degree_Name=data['degree_name'],category=data['program_category'],branch=data['branch_name'])
    x=db.save()
    return HttpResponse('{"status":"success"}')

def findinstitute(request): 
    mymembers = Course.objects.all().values()   
    data={'courselist':mymembers}
    return selectcourse(request,"findinstitute.html",data)

def editinstitute(request):
    data=request.POST
    db=Course.objects.values_list('id','institute_Code','program_code','type','institute_Name','degree_Name','category','branch').filter(id=data['uid'])
    print(db[0])
    data={
    'courselist':db[0]}
    return selectcourse(request,"editinstitute.html",data)

def deleteinstitute(request):
    data=request.POST
    member = Course.objects.get(id=data['uid'])
    member.delete()
    print(member)
    return HttpResponse('{"status":"success"}')


# ================  STUDENT PROFILE ==========================

def doeditinstitute(request):
    data=request.POST
    mydb.commit()

    v=Course.objects.filter(id=data['uid']).update(institute_Code=data['institute_code'],program_code=data['program_code'],type=data['program_type'],institute_Name=data['institute_name'],degree_Name=data['degree_name'],category=data['program_category'],branch=data['branch_name'])
    if(v==1):
        return HttpResponse('{"status":"success"}')
    else: return HttpResponse('{"status":"fail"}')


def addstudent(request):
    data={}
    mydata = StudentDetails.objects.all().values()
    print(mydata)

    return selectcourse(request,"addstudent.html",data)

def doaddstudent(request):
    data=request.POST

    sql1 = "INSERT INTO student_marks (enrollment) VALUES ('"+data['enrollment']+"')"
    mycursor.execute(sql1)
    mydb.commit()
    x=mycursor.rowcount

    d=StudentDetails(enrollment=data['enrollment'],sem=data['sem'],roll=data['roll'],oldenrollment=data['oldenrollment'],name=data['name'],phone=data['phone'],email=data['email'],gender=data['gender'],dob=data['dob'],caste=data['caste'],subcast=data['subcast'],category=data['category'],password=data['password'],photo=data['photo'],institute_code=data['institute_code'],program_code=data['program_code'],parent_contact=data['parent_contact'],emergency_contact=data['emergency_contact'],userid=data['userid'],address=data['address'],aadhaar=data['aadhaar'],finalsem=data['finalsem'],term_end=data['term_end'],total_credits=data['total_credits'],total_grade_points=data['total_grade_points'],total_backlog=data['total_backlog'])
    d.save()

    if(x==1):
         return HttpResponse('{"status":"success"}')
    else: return HttpResponse('{"status":"fail"}')

    


#================== EXCEL =========================================


def selectexcel(request):
    data={}
    return selectcourse(request,"excelupload.html",data)

def generateexcel(request):
    data=request.POST
    
    wb = Workbook()
    dest_filename = 'addstudent.xlsx'
    ws1 = wb.active
    ws1.title = "Students Detail"
    i=1
    x=[]
    for d in data:
        x.append(data[d])
    
    for i in range(0,len(x)-1):
        ws1.cell(1,i+1).value=x[i]
    wb.save(filename = dest_filename) 
    return HttpResponse("success")
    
   

def downloadexcel(request):
    with open(('addstudent.xlsx'), 'rb') as f:
        data = f.read()     
    response = HttpResponse(data, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="addstudent.xlsx"'
    return response

def uploadexcel(request):
    global fields
    if "GET" == request.method:
        return render(request, 'myapp/index.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        wb = openpyxl.load_workbook(excel_file)

        worksheet = wb["Students Detail"]
        print(worksheet)

        excel_data = list()

        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
        
        for i in fields:
            if (i not in excel_data[0]):
                print("not exists")
            else:
                print("exists")
        
        
        for i in excel_data:
            print(i)

        # return render(request, 'myapp/index.html', {"excel_data":excel_data})
        return HttpResponse("successs")


    