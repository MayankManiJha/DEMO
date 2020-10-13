from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from myapp.models import Dreamreal



# Create your views here.

def hello(request):
    text="""<h1>This is my app</h1>"""
    return HttpResponse(text)


def morning(request):
    #return render(request,"morning.html",{})
    return render(request,'morning.html')

def var(request):
    #return HttpResponse("<h1>The Value is : %s </h1>")
    return redirect(master_slave)

def dynPage(request):
    today=datetime.now().date()
    weekdays=['mon','tue','wed','thrus','fri','sat','sun']
    return render(request,"code.html",{"today":today,"weekdays":weekdays})

def master_slave(request):
    today=datetime.now()
    return render(request,"Page-Slave.html",{"today":today})


def crudops(request):
    dr1= Dreamreal(
        website= 'www.abc.com',
        mail='xyz@abc.com',
        name='abc',
        phonenumber="1234567890"
    )
    dr1.save()
    # objects= Dreamreal.objects.all()
    # res='Printing all entries from DB: <br>'
    # for data in objects:
    #     res+= data.name+"<br>"
    # return HttpResponse(res)


