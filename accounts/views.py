from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth


# Create your views here.
def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,"login.html")
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password = request.POST['password1']
        if password==password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            user = User.objects.create_user(username=username, password=password)
            user.save();
            print("user created")
        else:
            print("password not matched")
            return redirect('register')
        return redirect('/')

    else:

        return render(request,'registration.html')
