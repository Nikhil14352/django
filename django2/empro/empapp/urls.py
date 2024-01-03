from django.urls import path
from .import views

urlpatterns = [
    path('',views.empapp,name='empapp'),
    path('display',views.dispaly,name='empapp'),
]