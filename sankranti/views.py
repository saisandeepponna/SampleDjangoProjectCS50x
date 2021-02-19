
import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    n=datetime.datetime.now()
    return render(request,'sankranti/index.html',{"sankrant":n.month==1 and n.day==14})
