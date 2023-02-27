from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .models import place,actors


# Create your views here.

def demo(request):
    obj=place.objects.all()
    obj1=actors.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})