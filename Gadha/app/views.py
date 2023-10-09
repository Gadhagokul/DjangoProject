from django.shortcuts import render,redirect
from .forms import student
from .models import user1
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'home.html')
def addshow(request):
    if request.method=='POST':
        fm=student(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=student()
    stud=user1.objects.all()
    return render(request,'addshow.html',{'form':fm,'stu':stud})

def deletedata(request,id):
    if request.method == 'POST':
        dl=user1.objects.get(pk=id)
        dl.delete()
    return HttpResponseRedirect('/add')

def update(request,id):
    if request.method=='POST':
        up=user1.objects.get(pk=id)
        fm=student(request.POST,instance=up)
        if fm.is_valid():
            fm.save()
        else: up=user1.objects.get(pk=id)
        fm=student(instance=up)
    return render(request,'update.html',{'form':fm})
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('login')
    return render(request,'register.html')
def login1(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/add')
        else:
            return redirect('register')
    return render(request,'login.html')
def logout1(request):
    logout(request)
    return redirect('/')