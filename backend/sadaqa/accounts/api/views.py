from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from .serializers import *
from accounts.models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator

####################################---------  admin panel / view all user data  -------------###################################
class ListMyUser(generics.ListAPIView):
    permission_classes=(IsAdminUser,)
    authentication_classes=(TokenAuthentication,)
    queryset= MyUser.objects.all()
    serializer_class=MyUserSerilizers

####################################---------  register  -------------###################################
@method_decorator(csrf_exempt, name='dispatch')
class RegisterUserAPIView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

####################################---------  login  -------------###################################
@permission_classes([AllowAny])
@api_view(['POST'])
def user_login(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username, password=password)
    if user :
        if user.is_email_verified or user.is_superuser:
            login(request, user)
            return Response({"success": "Logged in successfully."}, status=200)
        return Response({'error': 'Email is not activated',"email":user.email}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            
####################################---------  logout  -------------###################################
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def user_logout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response('User Logged out successfully',200)    




class RetrieveUpdateDestroyMyUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(AllowAny,)
    authentication_classes=(TokenAuthentication,)
    queryset= MyUser.objects.all()
    serializer_class=MyUserSerilizers


