from rest_framework import generics
from tracks.models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import AllowAny


class TrackList(generics.ListCreateAPIView):
    permission_classes=(AllowAny,)
    authentication_classes=(SessionAuthentication, TokenAuthentication)
    queryset = Track.objects.all()
    serializer_class = TrackSerializers

class TrackAllCRUD(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(AllowAny,)
    authentication_classes=(SessionAuthentication, TokenAuthentication)
    queryset = Track.objects.all()
    serializer_class = TrackSerializers
    
