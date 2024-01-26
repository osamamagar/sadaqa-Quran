from rest_framework import serializers
from accounts.models import *
from rest_framework.response import Response
from django.utils.crypto import get_random_string
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class MyUserSerilizers(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name', read_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'first_name', 'last_name', 'username', 'phone', 'email', 'image', 'birth_date',
                  'facebook_profile', 'country', 'country_name')

        extra_kwargs = {
            'id': {'read_only': True},
            'username': {'read_only': True},
            'is_email_verified': {'read_only': True},
            'created_at': {'read_only': True}, }

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
        validators=[UniqueValidator(queryset=MyUser.objects.all())])
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = MyUser
        fields = ('username', 'password', 'password2',
                'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = MyUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            activation_code=get_random_string(6),  # Generate activation code
        )
        
        user.set_password(validated_data['password'])
        user.save()
        return user



