from django.db import models

# Create your models here.

class Departments(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName = models.CharField( max_length=500)

class Employees(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    EmployeeName = models.CharField( max_length=500)
    Department = models.CharField( max_length=500)
    DateOfJoin= models.DateField()
    ProfileFileName =models.CharField(max_length=500)