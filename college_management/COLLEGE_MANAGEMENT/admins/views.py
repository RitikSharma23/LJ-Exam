from django.shortcuts import render

# Create your views here.

def dashboard(request):
  return render(request,'Admin/dashboard.html',{})
def subadmin(request):
  return render(request,'Admin/subadmin.html',{})
def subadminAdd(request):
  return render(request,'Admin/subadmin-add.html',{})
def subadminEdit(request):
  return render(request,'Admin/subadmin-edit.html',{})
def subject(request):
  return render(request,'Admin/subject.html',{})
def subjectAdd(request):
  return render(request,'Admin/subject-add.html',{})
def subjectEdit(request):
  return render(request,'Admin/subject-edit.html',{})
def setting(request):
  return render(request,'Admin/setting.html',{})
