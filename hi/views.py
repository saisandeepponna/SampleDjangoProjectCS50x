from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"hi/index.html")
def sai(request):
     return HttpResponse("hello sai!")
def greet(request,name):
    return HttpResponse(f"hi {name.capitalize()}")