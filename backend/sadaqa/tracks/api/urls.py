from django.urls import path
from .views import *



urlpatterns=[
    path('tracks/',TrackList.as_view(),name='TrackList'),
    path('tracks/<int:pk>/', DetailTrack.as_view(), name="DetailTrack"),
    path('comments/', ListComment.as_view(), name="ListComment"),
    path('comments/<int:pk>/', DetailComment.as_view(), name="DetailComment"),
    path('reply/', ReplyList.as_view(), name="ReplyList"),
    path('reply/<int:pk>/', DetailReply.as_view(), name="DetailReply"),

]