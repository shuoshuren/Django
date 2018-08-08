from django.shortcuts import render,HttpResponse

# Create your views here.

def index(reuest):
    return HttpResponse("hello world")


def detail(request,year,month,day):
    return HttpResponse("year:%s,month:%s,day:%s" %( year,month,day))