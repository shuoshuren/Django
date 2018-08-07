from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    # list = BookInfo.books.filter(heroinfo__hcontent__contains='八')
    list = BookInfo.books.filter(pk__lt = 3)
    context = {'list':list}
    return render(request,'booktest/index.html',context)
