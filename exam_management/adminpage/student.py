from .views import *


def addstudent(request):
    
    return render(request,"addstudent.html",{})

def doaddstudent(request):
    data=request.POST

    val=data['enrollment'],data['sem'],data['roll'],data['oldenrollment'],data['name'],data['phone'],data['email'],data['gender'],data['dob'],data['caste'],data['subcast'],data['category'],data['photo'],data['institute_code'],data['program_code'],data['parent_contact'],data['emergency_contact'],data['userid'],data['address'],data['aadhaar'],data['finalsem'],data['term_end'],data['total_credits'],data['total_grade_points'],data['total_backlog']   
    
    sql = "INSERT INTO student_details (enrollment,sem,roll,oldenrollment,name,phone,email,gender,dob,caste,subcast,category,photo,institute_code,program_code,parent_contact,emergency_contact,userid,address,aadhaar,finalsem,term_end,total_credits,total_grade_points,total_backlog)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    
    mycursor.execute(sql,val)
    x=mycursor.rowcount
    mydb.commit()
    if(x==1):
         return HttpResponse('{"status":"success"}')
    else: return HttpResponse('{"status":"fail"}')