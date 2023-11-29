from rest_framework.response import Response
from rest_framework import generics
from tracks.models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import AllowAny,  IsAuthenticatedOrReadOnly



class ListComment(generics.ListCreateAPIView):
    permission_classes=(AllowAny,)
    authentication_classes=(SessionAuthentication, TokenAuthentication)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

    def list(self,request,*args,**kwargs):
        queryset= self.get_queryset()
        serializer = self.get_serializer(queryset,many=True)

        for comment in serializer.data:
            comments_id = comment['id']
            comment['Replies']= ReplySerializers(
                ReplyComment.objects.filter(comment_id=comments_id), 
                many=True, context=self.get_serializer_context()).data
        return Response({"comments": serializer.data})

class DetailComment(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(AllowAny,)
    authentication_classes=(SessionAuthentication, TokenAuthentication)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers


class TrackList(generics.ListCreateAPIView):
    permission_classes=(AllowAny,)
    authentication_classes=(SessionAuthentication, TokenAuthentication)
    queryset = Track.objects.all()
    serializer_class = TrackSerializers

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        for track in serializer.data:
            tracks_id = track['id']
            track ['comments']=CommentSerializers(
                Comment.objects.filter(track_id=tracks_id),
                many=True, context=self.get_serializer_context()).data
        return Response(serializer.data)



    

class DetailTrack(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(AllowAny,)
    authentication_classes=(SessionAuthentication, TokenAuthentication)
    queryset = Track.objects.all()
    serializer_class = TrackSerializers

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response([serializer.data,CommentSerializers(
            Comment.objects.filter(track_id=instance.id),many=True
        ).data])


class ReplyList(generics.ListCreateAPIView):
    permission_classes=(AllowAny,)
    authentication_classes=(SessionAuthentication, TokenAuthentication)
    queryset = ReplyComment.objects.all()
    serializer_class = ReplySerializers



class DetailReply(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(AllowAny,)
    authentication_classes=(SessionAuthentication, TokenAuthentication)
    queryset = ReplyComment.objects.all()
    serializer_class = ReplySerializers
