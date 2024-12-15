from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    x=2
    y=3
    return x

# Create your views here.
def say_hello(request):
    # pull data from db
    # treansfrom
    # send email
    # return HttpResponse('hello world')
    x = calculate()
    return render(request, "hello.html", {"name": "charith"})
