from django.db import models

class StudentDetails(models.Model):
    enrollment=models.CharField(max_length=16,primary_key=True)
    name=models.CharField(max_length=70,null=True)
    sem=models.CharField(null=True,max_length=20)
    phone=models.CharField(max_length=10,null=True,unique=True)
    roll=models.CharField(null=True,blank=True,max_length=10)
    oldenrollment=models.CharField(max_length=16,null=True)
    email=models.CharField(max_length=70,null=True)
    gender=models.CharField(max_length=1,null=True)
    dob=models.DateTimeField(null=True,blank=True)
    caste=models.CharField(max_length=20,null=True)
    subcast=models.CharField(max_length=20,null=True)
    category=models.CharField(max_length=10,null=True)
    password=models.CharField(max_length=30,null=True)
    photo=models.CharField(max_length=20,null=True)
    institute_code=models.CharField(max_length=6,null=True)
    program_code=models.CharField(max_length=6,null=True)
    parent_contact=models.CharField(max_length=10,null=True)
    emergency_contact=models.CharField(max_length=10,null=True)
    userid=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=200,null=True)
    aadhaar=models.CharField(max_length=12,null=True)
    finalsem=models.CharField(null=True,max_length=10)
    term_end=models.CharField(null=True,max_length=4)
    total_credits=models.FloatField(null=True)
    total_grade_points=models.FloatField(null=True)
    total_backlog=models.IntegerField(null=True)


class Course(models.Model):
    id=models.AutoField(primary_key=True)
    institute_Code=models.CharField(max_length=6)
    program_code=models.CharField(max_length=6)
    type=models.IntegerField()
    institute_Name=models.CharField(max_length=100)
    degree_Name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    branch =models.CharField(max_length=100)

class StudentMarks(models.Model):
    enrollment=models.CharField(max_length=16,primary_key=True)

    
class Subject(models.Model):
    subjectcode=models.CharField(max_length=10,primary_key=True)
    sem=models.IntegerField()
    subjectname=models.CharField(max_length=20)
    theory=models.BooleanField(default=False)
    theory_marks=models.IntegerField(default=0)
    practical=models.BooleanField(default=False)
    practical_marks=models.IntegerField(default=0)
    mid=models.BooleanField(default=False)
    mid_marks=models.IntegerField(default=0)
    institute_code=models.CharField(max_length=6,null=True)
    program_code=models.CharField(max_length=6,null=True)
    credit=models.IntegerField(default=0)

class Grade(models.Model):
    r1=models.IntegerField()
    r2=models.IntegerField()
    gradepoint=models.FloatField()
    grade=models.CharField(max_length=6)
    gradeclass=models.CharField(max_length=50)
    