# from django.shortcuts import render
# import requests
# from .models import City
# from .forms import CityForm


# def index(request):
#     url = ("https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID={}")
#     #cities=City.objects.all()
#     if request.method == "POST":
#         form=CityForm(request.POST)
#         form.save()
#     form=CityForm
#     weather_data=[]
#     for villages in City.objects.all():
#         r = requests.get(url.format(villages,'1225f09c1a0407c6edd97e9f8f47baad')).json()
#         print(r)
#         weather = {
#             'city' : villages,
#             'temperature' : r['main']['temp'],
#             'description' : r['weather'][0]['description'],
#             'icon' : r['weather'][0]['icon']
#         }
#         weather_data.append(weather)
        
#         context = {'weather_data' : weather_data,'form':form}

#     return render(request, 'index.html',context,)
    

from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    url = ("https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=1225f09c1a0407c6edd97e9f8f47baad")
    if request.method == "POST":
        form=CityForm(request.POST)
        form.save()
    form=CityForm
    weather_data=[]
    for villages in City.objects.all():
        r = requests.get(url.format(villages,)).json()
        print(r)
        weather = {
            'city' : villages,
            'temperature' : ((r['main']['temp'])-32)*5/9,
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon']
        }
        weather_data.append(weather)
        
        context = {'weather_data' : weather_data,'form':form}

    return render(request, 'index.html',context,)