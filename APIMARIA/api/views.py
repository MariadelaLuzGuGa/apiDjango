"""
Codigo en Vista para el Login
"""
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    """a"""
    return render (request, 'home.html')
    
def SignupPage(request):
    """b"""
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            messages.error(request, "Las contraseñas no coinciden vuelve a escribirlas")
            # return HttpResponse("La Contraseña no coincide")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render (request,'registro.html')

def LoginPage(request):
    """c"""
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        # print(username,pass1)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'El Usuario o Contraseña son incorrectos. Vuelva a ingresarlos')
            # return HttpResponse ("El Usuario o Contraseña son Incorrectos")
    return render (request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')