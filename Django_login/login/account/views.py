from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Signin,SignUp
from django.contrib import messages
from login.settings import *
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'account/index.html')

def signout(request):
    logout(request)
    messages.success(request, "Logout Succesful")
    return redirect('http://127.0.0.1:8000')

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['password']

        user=authenticate(username=username, password=pass1)
        
        user_model=Signin(Username=username)
        user_model.save()
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return render(request,'account/index.html', {"fname":user.first_name})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('https://127.0.0.1:8000')
        
    return render(request, 'account/signin.html')

def signup(request):
    if request.method=="POST":
        name=request.POST["username"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        mail=request.POST["mail"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]

        if User.objects.filter(username=name).exists():
            messages.error(request,"Username already exists")
            return redirect('http://127.0.0.1:8000/signup')

        if User.objects.filter(email=mail).exists():
            messages.error(request,"Email already exists")
            return redirect('http://127.0.0.1:8000/signup')

        if not pass1 == pass2:
            messages.error(request,"Password does not match")
            return redirect('http://127.0.0.1:8000/signup')

        if not name.isalnum():
            messages.error(request,"Username should only contains alphabet and numeric")
            return redirect('http://127.0.0.1:8000/signup')
        
        user = User.objects.create_user(username=name, email=mail, password=pass1)
        user.first_name=fname
        user.last_name=lname
        # user.is_active=False
        user.save()

        user_model=SignUp(name=name, mail=mail)
        user_model.save()

        # sending mail
        subject = "Welcome to custom based email sending mechanism"
        message = f"hello {fname}!\n Congratulations on successful registration.\nUsername:- {name} \nEmail:- {mail}"
        sender = EMAIL_HOST_USER
        reciever = [user.email,]
        is_sent = send_mail(subject=subject, message=message, from_email=sender, recipient_list=reciever)
        print(is_sent)

        messages.success(request, "An email is sent to your email id")
        return redirect('http://127.0.0.1:8000/success')
    
    return render(request, 'account/signup.html')

def reg_success(request):
    return render(request,'account/signup_completion.html')
