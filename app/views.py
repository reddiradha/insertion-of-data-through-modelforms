from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TD=TopicForm(request.POST)
        if TD.is_valid():
            TD.save()
            return HttpResponse('Topic data is inserted successfully')

    return render (request,'insert_topic.html',d)
      

def insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}
    if request.method=='POST':
        WD=WebpageForm(request.POST)
        if WD.is_valid(): 
            WD.save()
            return HttpResponse('Webpage data is inserted successfully')

    return render (request,'insert_webpage.html',d)
    
def insert_access(request):
    AFO=AccessrecordForm()
    d={'AFO':AFO}
    if request.method=='POST':
        AD=AccessrecordForm(request.POST)
        if AD.is_valid(): 
            AD.save()
            return HttpResponse('Access records data is inserted successfully')

    return render (request,'insert_access.html',d)
    
     

    