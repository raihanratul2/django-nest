from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home',),
    path('endgame',endgame,name='endgame',),
    path('signup',signup,name='signup',),
    path('signin',signin,name='signin',),
]