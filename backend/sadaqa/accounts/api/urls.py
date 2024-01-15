from django.urls import path
from .views import *


urlpatterns=[
    path("get_all_user/",ListMyUser.as_view()),
    path("registration/",CreateMyUser.as_view()),
    path('edit_user/<int:pk>/',RetrieveUpdateDestroyMyUser.as_view()),

    
]