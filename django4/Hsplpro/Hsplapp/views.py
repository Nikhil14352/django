from django.shortcuts import render
from .models import PatientDetails

# Create your views here.
def Hsplapp(request):
    if request.method == "POST":
        patientname=request.POST["patientname"]
        doj=request.POST["doj"]
        gender=request.POST["gender"]
        mobileNo=request.POST["mobileNo"]
        problem=request.POST["problem"]
        address=request.POST["address"]
        
        Patients=PatientDetails(patientname=patientname,doj=doj,gender=gender,mobileNo=mobileNo,problem=problem,address=address)
        Patients.save()
        

    return render(request,"index.html",)

def display(request):
    std=PatientDetails.objects.all()
    return render(request,'display.html',{'Patients':std})



