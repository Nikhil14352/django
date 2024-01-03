from django.shortcuts import render
from .models import students

# Create your views here.
def myApp(request):
    if request.method=="POST":
        name=request.POST['name']
        branch=request.POST['branch']
        college=request.POST['college']
        grade=request.POST['grade']
        std=students(name=name,branch=branch,college=college,grade=grade)
        std.save()
        
        


        
    return render(request,'index.html')

def display(request):
    stu=students.objects.all()
    return render(request,"display.html",{"std":stu})




