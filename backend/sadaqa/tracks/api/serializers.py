from rest_framework import serializers
from tracks.models import *



class CommentSerializers(serializers.ModelSerializer):
    user_name=serializers.CharField(source='user.username', read_only=True)
    track_name= serializers.CharField(source='track.name',read_only=True)
    class Meta:
        model = Comment
        fields = ('id','content','track','track_name','user','user_name','commentLike')


class TrackSerializers(serializers.ModelSerializer):
    user_name=serializers.CharField(source ='user.username',read_only=True)
    comments = CommentSerializers(many=True, read_only=True)

    class Meta:
        model = Track
        fields = ('id','name','audio','description','image','user','user_name','likes','views','comments')


class ReplySerializers(serializers.ModelSerializer):
    commenter_name = serializers.CharField(source='comment.user.username', read_only=True)
    class Meta:
        model = ReplyComment
        fields = ('id','user','commenter_name','comment','replyLike','replyContent')
