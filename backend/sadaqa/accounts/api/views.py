from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from accounts.models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics


class ListMyUser(generics.ListAPIView):
    permission_classes=(AllowAny,)
    authentication_classes=(TokenAuthentication,)
    queryset= MyUser.objects.all()
    serializer_class=MyUserSerilizers


class CreateMyUser(generics.CreateAPIView):
    permission_classes=(AllowAny,)
    authentication_classes=(TokenAuthentication,)
    queryset= MyUser.objects.all()
    serializer_class=UserRegistrationSerializers


class RetrieveUpdateDestroyMyUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(AllowAny,)
    authentication_classes=(TokenAuthentication,)
    queryset= MyUser.objects.all()
    serializer_class=MyUserSerilizers


