from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    else:
        return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password1']
        confirm_password=request.POST['password2']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"USERNAME NOT AVAILABLE")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"EMAIL ALREADY EXISTS")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"password not match")
    return render(request,"registration.html")