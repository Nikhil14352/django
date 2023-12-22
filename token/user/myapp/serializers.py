from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Student

class SignupSerializer(serializers.ModelSerializer):
    def create(self,validated_data):
        validated_data['password']=make_password(validated_data.get('password'))
        return super(SignupSerializer,self).create(validated_data)
    

    
    class meta:
        model=User
        fields=['username','password']

class LoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField()
    
    class Meta:
        model=User
        fields=['username','password']

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields=['name','email','created_at','updated_at']
