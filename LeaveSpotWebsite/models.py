from django.db import models

# Create your models here.

class InsertStudent(models.Model):
    Name = models.CharField(max_length = 100)
    Id = models.CharField(max_length = 12)
    Course = models.CharField(max_length = 5)
    Semester = models.CharField(max_length = 1)
    Section = models.CharField(max_length = 1)
    Email_Id = models.CharField(max_length = 100)
    Password = models.CharField(max_length = 100)
    class Meta:
        db_table = "student"

class InsertCoordinator(models.Model):
    Id = models.CharField(max_length = 2)
    Name = models.CharField(max_length = 100)
    Course = models.CharField(max_length = 5)
    Semester = models.CharField(max_length = 1)
    Section = models.CharField(max_length = 1)
    Email_Id = models.CharField(max_length = 100)
    Password = models.CharField(max_length = 100)
    class Meta:
        db_table = "coordinator"

class InsertStudentLeave(models.Model):
    Id = models.CharField(max_length = 12, primary_key=False)
    Name = models.CharField(max_length = 100)
    Course = models.CharField(max_length = 5)
    Semester = models.CharField(max_length = 1)
    Section = models.CharField(max_length = 1)
    No_of_Leaves = models.CharField(max_length = 2)
    Reason = models.CharField(max_length = 200)
    Dated = models.CharField(max_length = 100)
    Doc_Req = models.CharField(max_length = 12)
    Status = models.CharField(max_length = 12)
    class Meta:
        db_table = "student_leave"