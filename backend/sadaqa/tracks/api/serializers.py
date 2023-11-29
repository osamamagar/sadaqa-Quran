from rest_framework import serializers
from tracks.models import *

class TrackSerializers(serializers.ModelSerializer):
    user_name=serializers.CharField(source ='user.username',read_only=True)

    class Meta:
        model = Track
        fields = ('id','name','audio','description','image','user','user_name','likes','views')