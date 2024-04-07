from django.shortcuts import render,HttpResponseRedirect
from django.contrib import auth
from django.contrib.messages import success,error
from .models import Todo
from django.contrib.auth.forms import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/')
def add_item(request):
    if (request.method=='POST'):
        task=request.POST.get('task')
        description=request.POST.get('description')
        date=request.POST.get('date')
        t=Todo()
        t.user=request.user
        t.task_name=task
        t.description=description
        t.date=date
        t.save()
    return render(request,'addItem.html')

@login_required(login_url='/')
def show_item(request):
    objects=Todo.objects.filter(user=request.user)
    return render(request,'showItem.html',{'data':objects})

def delete_item(request,pk):
    object=Todo.objects.get(id=pk)
    object.delete()
    objects = Todo.objects.filter(user=request.user)
    return render(request, 'showItem.html', {'data': objects})

@login_required(login_url='/')
def update_item(request,pk):
     object=Todo.objects.get(id=pk)
     if (request.method == 'POST'):
         object.user=request.user
         object.task_name = request.POST.get('task')
         object.description=request.POST.get('description')
         object.is_completed=request.POST.get('status')
         #object.date=request.POST.get('date')
         object.save()
         error(request,"Data Updated")
     return render(request, 'updateItem.html',{'data':object})

def login(request):
    if(request.method=='POST'):
        lname=request.POST.get('uname')
        lpward=request.POST.get('psw')
        user=auth.authenticate(username=lname,password=lpward)
        if(user is not None):
            auth.login(request,user)
            if(user.is_superuser):
                return HttpResponseRedirect('additem/')
            else:
                return HttpResponseRedirect('additem/')
        else:
            error(request,"Invalid User")
    return render(request,'index.html')

def signup(request):
    if(request.method=='POST'):
        uname=request.POST.get('uname')
        try:
            match = User.objects.get(username=str(uname))
            if (match):
                error(request, "Username Already Exist")
        except:
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            mail = request.POST.get('email')
            org=request.POST.get('org')
            pward = request.POST.get('pward')
            cpward = request.POST.get('cpward')
            if pward == cpward:
                User.objects.create_user(username=str(uname),
                                         first_name=str(fname),
                                         last_name=str(lname),
                                         email=mail,
                                         password=pward
                                         )
                return HttpResponseRedirect('/')
            else:
                error(request, "Password and Confirm Password not Matched")
    return render(request, "Signup.html")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')