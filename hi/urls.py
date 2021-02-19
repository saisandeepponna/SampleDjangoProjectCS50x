from django.urls import path
from . import views

urlpatterns=  [path("",views.index,name="index"),path("sai",views.sai,name="sai"),
               path("<str:nam>",views.greet,name="greet")]