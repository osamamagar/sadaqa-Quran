from django.urls import path
from .views import *



urlpatterns=[
    path('tracks/',TrackList.as_view(),name='TrackList'),
    path('tracks/<int:pk>/', TrackAllCRUD.as_view(), name="TrackAllCRUD"),
]