from django.shortcuts import render
from .models import Employee
from .serializers import Employeeserializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
# Create your views here.
@api_view(['GET','POST'])
def employee_data(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = Employeeserializers(employee,many=True)
        return JsonResponse(serializer.data, safe = False)
    if request.method == 'POST':
        serializer = Employee(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','POST','DELETE'])
def employee_details(request,id):
    try:
       employee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Employeeserializers(employee)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = Employeeserializers(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 