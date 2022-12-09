from django.shortcuts import render,HttpResponse
from adminpage.models import *
from openpyxl import Workbook
import openpyxl

# Create your views here.

def markshome(request):
    d=Subject.objects.all().values()
    details={'subjectlist':d}
    return render(request,"marks.html",details)

def adminpage(request):
    return render(request,"admin.html",{})

def marksoption(request):
    data=request.POST
    print(data)
    d=Subject.objects.filter(subjectcode=data['subjectcode']).values()
    details={'subject':d[0],'year':data['year']}
    return render(request,"marksoption.html",details)


def theory(request):
    data=request.POST
    d=Subject.objects.filter(subjectcode=data['subjectcode']).values()
    details={
        'subject':d[0],'year':data['year'],'type':data['type']
    }
    return render(request,"theory.html",details)


def uploadtheory(request):
    if "GET" == request.method:
        return render(request, 'myapp/index.html', {})
    else:
        excel_file = request.FILES["theoryexcel"]

        wb = openpyxl.load_workbook(excel_file)

        worksheet = wb["Students Seat"]

        excel_data = list()

        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
        
        
        detail={'excel':excel_data}

        print(excel_data[0])
 
        # return render(request,"viewexcel.html",detail)
        return HttpResponse(excel_data)