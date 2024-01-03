from django.db import models

# Create your models here.

class PatientDetails(models.Model):
    patientname=models.CharField(max_length=100)
    doj=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    mobileNo=models.CharField(max_length=100)
    problem=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
  
