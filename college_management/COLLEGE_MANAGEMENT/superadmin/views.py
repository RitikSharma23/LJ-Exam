from django.shortcuts import render

def dashboard(request):
  
  return render(request, 'dashboard.html',{})

def branch(request):
  
  return render(request, 'branch.html',{})

def branchAdd(request):
  
  return render(request, 'branch-add.html',{})

def branchEdit(request):
  
  return render(request, 'branch-edit.html',{})

def course(request):
  
  return render(request, 'course.html',{})

def admins(request):
  
  return render(request, 'admin.html',{})

def setting(request):
  
  return render(request, 'setting.html',{})