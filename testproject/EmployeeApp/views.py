from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializer import DepartmentSerializer,EmployeeSerializer
# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments=Departments.objects.all()
        departments_serialzer=DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serialzer.data,safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serialzer=DepartmentSerializer(data=department_data)
        if departments_serialzer.is_valid():
            departments_serialzer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Fail",safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Departments.objects.get(DepartmentID=department_data['DepartmentID'])
        departments_serialzer=DepartmentSerializer(department,data=department_data)
        if departments_serialzer.is_valid():
            departments_serialzer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentID=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    








