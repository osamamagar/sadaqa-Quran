from django.urls import path
from .views import *


urlpatterns=[
    path("list_regular_user/",ListMyUser.as_view()),
    path("registration/",RegisterUserAPIView.as_view()),
    path('edit_regular_user/<int:pk>/',RetrieveUpdateDestroyMyUser.as_view()),
    path('login/', user_login, name='user-login'),

    
]