from django.urls import path
from .import views
urlpatterns = [
    path('',views.myApp,name="myApp"),
    path('display',views.display,name="myApp")
]
