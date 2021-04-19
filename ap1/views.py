from django.shortcuts import render
from django.contrib.auth.models import User
from .models import myuser
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def sinup(requset):
    if requset.method=='POST':
        username=requset.POST['myname']
        email=requset.POST['email']
        password=requset.POST['password']
        user=User.objects.create_user(username=username,password=password,email=email)
        user.save()
        add = requset.POST['add']
        phon = requset.POST['phone']
        my=myuser( address=add,phon=phon,user=user)
        my.save()
        print(username,password,email,add,phon)
        return render(requset,'login.html')

    return render(requset,'sinup.html')

def login(requset):
    if requset.method=='POST':
        username=requset.POST['myname']
        password=requset.POST['password']
        #print(username,password)
        user = authenticate(username=username, password=password)
        if user is not None:
            return render(requset,'done.html')
        else:
            return render(requset,'login.html')

    return render(requset,'login.html')

@login_required(login_url='login')
def done(requset):
    data=myuser.objects.filter(user=requset.user)

    print(data)

    return render(requset,'done.html',{'data':data})
