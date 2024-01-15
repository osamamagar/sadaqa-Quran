from rest_framework import serializers
from accounts.models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password



class MyUserSerilizers(serializers.ModelSerializer):
    # country_name =serializers.CharField(source='country.name',read_only=True)


    class Meta:
        model = MyUser
        fields = ('id','first_name','last_name', 'username','phone','email','image','birth_date',
                  'facebook_profile','country')
        # fields = '__all__'

  
        
class UserRegistrationSerializers(serializers.ModelSerializer):
    country_name =serializers.CharField(source='country.name',read_only=True)
    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'username', 'password', 'email', 'birth_date', 'country_name')
        extra_kwargs = {'first_name': {'required': True}, 'last_name': {'required': True}}


