from django.contrib import admin
from EmployeeApp.models import Employees,Departments
# Register your models here.

admin.site.register(Departments)
admin.site.register(Employees)
