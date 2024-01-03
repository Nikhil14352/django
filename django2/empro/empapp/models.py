from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    mobileNo=models.CharField(max_length=100)
    domain=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    salary=models.CharField(max_length=100)
