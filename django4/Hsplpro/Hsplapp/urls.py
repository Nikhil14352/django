from django.urls import path
from .import views

urlpatterns = [
    path('',views.Hsplapp,name='Hsplapp'),
    path('display',views.display,name='Hsplapp')
]