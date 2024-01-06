from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    ETFO=TopicForm()
    #Empty Topic Form Object
    d={'ETF':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        #Topic Form Data Object
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('data is inserted in topic ')
    return render(request,'insert_topic.html',d)   

def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWF':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()   
            return HttpResponse('data is inserted in webpage') 
    return render(request,'insert_webpage.html',d)           

def insert_accessrecord(request):
    EAFO=AccessRecordForm()
    d={'EAF':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()   
            return HttpResponse('data is inserted in accessrecord') 
    return render(request,'insert_accessrecord.html',d)           
