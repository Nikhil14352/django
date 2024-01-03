from django.shortcuts import render
from .models import EmployeeDetails

# Create your views here.
def empapp(request):
    if request.method == "POST":
        firstName=request.POST["firstName"]
        lastName=request.POST["lastName"]
        email=request.POST["email"]
        dob=request.POST["dob"]
        gender=request.POST["gender"]
        mobileNo=request.POST["mobileNo"]
        domain=request.POST["domain"]
        company=request.POST["company"]
        salary=request.POST["salary"]
        employess=EmployeeDetails(firstName=firstName,lastName=lastName,email=email,dob=dob,gender=gender,mobileNo=mobileNo,domain=domain,company=company,salary=salary)
        employess.save()
        

    return render(request,"index.html")

def dispaly(request):
    std=EmployeeDetails.objects.all()
    return render(request,"index.html",{"employess":std})