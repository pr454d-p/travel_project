from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,"Invalid username or Password")
            return redirect('login')
    return render(request,'login.html')

def sign_up(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        if password != confirm_password:
            messages.info(request,'Password does not match')
            return redirect('sign_up')
        elif User.objects.filter(username=user_name).exists():
            messages.info(request,'Username already used')
            return redirect('sign_up')
        elif User.objects.filter(email = email).exists():
            messages.info(request,'Email already used')
            return redirect('sign_up')
        else:
            user = User.objects.create_user(username=user_name,password=password,first_name=first_name,last_name=last_name,email=email)
            user.save()
            print(first_name,last_name,'created account')
            return redirect('login')
    else:    
        return render(request,'sign-up.html')