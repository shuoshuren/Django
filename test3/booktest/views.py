from django.shortcuts import render,HttpResponse

# Create your views here.

def index(reuest):
    return HttpResponse("hello world")


def detail(request,year,month,day):
    return HttpResponse("year:%s,month:%s,day:%s" %( year,month,day))

def getTest1(request):
    '''展示链接的页面'''
    return render(request,'booktest/getTest1.html')

def getTest2(request):
    '''接受一键一值的情况'''
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    context={'a':a,'b':b,'c':c}
    return render(request,'booktest/getTest2.html',context)

def getTest3(request):
    '''接收一键多值的清空'''
    a = request.GET.getlist('a')
    context= {'a': a}
    return render(request,'booktest/getTest3.html',context)