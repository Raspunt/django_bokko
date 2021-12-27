
from django.urls import path 
from . views import *


urlpatterns = [

    path("",MainPage,name="MainPageUrl"),
    path("login/",LoginPage,name="LoginUrl"),
    path("reg/",RegisterPage,name="RegUrl"),
    

]
