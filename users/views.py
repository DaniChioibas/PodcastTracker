from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .forms import CustomUserCreationForm

# Create your views here.

def profiles(request):
    return render(request, 'users/profiles.html')

def registerUser(request):
    page='register'
    form=CustomUserCreationForm
    context={'page': page,'form': form}

    if request.method=="POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'An error has occurred during registration')
            
    return render(request,'users/login_register.html',context)

def loginUser(request):

    page = 'login'
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request,'Username does not exist')
            return redirect('login')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request,'Username OR password is incorrect')
    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')