from django.shortcuts import render,HttpResponse
from adminpage.models import *
import mysql.connector
from openpyxl import Workbook
import openpyxl

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
    c=("SELECT enrollment,name FROM adminpage_studentdetails WHERE enrollment like '__"+str(d['institute_code'])+"_"+str(d['program_code'])+"%' and sem="+str(d['sem'])+";")
    print(c)
    mycursor.execute(c)
    myresult=[]
    myresult = mycursor.fetchall()

    wb = Workbook()
    dest_filename = 'Seat.xlsx'
    ws1 = wb.active
    ws1.title = "Students Seat"
    if(len(myresult)>1):
        for i in range(0,len(myresult)):
            ws1.cell(i+2,1).value=myresult[i][0]
            ws1.cell(i+3,2).value=myresult[i][1]
            ws1.cell(i+4,3).value=(data['session']+data['year'][2:]+data['subjectcode'][1:5]+str(d['sem'])+myresult[i][0][-3:])


        wb.save(filename = dest_filename) 

        wb.close()
        
        return HttpResponse('{"status":"success"}')
    else:return HttpResponse('{"status":"nodata"}')

def downloadseat(request):
    file_location = 'Seat.xlsx'

    try:    
        with open(file_location, 'rb') as f:
           file_data = f.read() 
        response = HttpResponse(file_data, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="sitting.xlsx"'

    except IOError:
        response = HttpResponse('<h1>File not exist</h1>')

    return response


def seatremedial(request):
    data=request.POST
    d=Subject.objects.filter(subjectcode=data['subjectcode']).values()
    myresult=[]
    d=d[0]
    b='{"Status": "F"%'
    sub=str(d['sem'])+"_"+d['subjectcode']+data['type']
    c=('SELECT  adminpage_studentmarks.enrollment,adminpage_studentdetails.name FROM adminpage_studentmarks INNER JOIN adminpage_studentdetails ON adminpage_studentdetails.enrollment=adminpage_studentmarks.enrollment WHERE '+str(sub)+' LIKE '+"'"+b+"'" )
    print(c)
    mycursor.execute(c)
    myresult = mycursor.fetchall()

    print(myresult)

    wb = Workbook()
    dest_filename = 'Seat.xlsx'
    ws1 = wb.active
    ws1.title = "Students Seat"
    if(len(myresult)>1):
        for i in range(0,len(myresult)):
            ws1.cell(i+1,1).value=myresult[i][0]
            ws1.cell(i+1,2).value=myresult[i][1]
            ws1.cell(i+1,3).value=(data['session']+data['year'][2:]+data['subjectcode'][1:5]+str(d['sem'])+myresult[i][0][-3:])

        wb.save(filename = dest_filename) 

        wb.close()
        
        return HttpResponse('{"status":"success"}')
    else:return HttpResponse('{"status":"nodata"}')

