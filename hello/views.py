from django.shortcuts import render

# Create your views here.
def index(request):
    A='hi'
    return render(request,'hello/index.html',{"l":A})
