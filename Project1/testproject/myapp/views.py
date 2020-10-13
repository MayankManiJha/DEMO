from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    text="""<h1>This is my app</h1>"""
    return HttpResponse(text)


def morning(request):
    #return render(request,"morning.html",{})
    return render(request,'morning.html')

def var(request):
    return HttpResponse("<h1>The Value is : %s </h1>")