from rest_framework.permissions import AllowAny, IsAdminUser
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


class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

class RetrieveUpdateDestroyMyUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(AllowAny,)
    authentication_classes=(TokenAuthentication,)
    queryset= MyUser.objects.all()
    serializer_class=MyUserSerilizers


class ListSuperuserMyUser(generics.ListAPIView):
    permission_classes = (IsAdminUser,)  # Assuming you have the IsAdminUser permission
    authentication_classes = (TokenAuthentication,)
    queryset = MyUser.objects.all()
    serializer_class = SuperuserMyUserSerializer

class RetrieveUpdateDestroySuperuserMyUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)  # Assuming you have the IsAdminUser permission
    authentication_classes = (TokenAuthentication,)
    queryset = MyUser.objects.all()
    serializer_class = SuperuserMyUserSerializer
