"""
Codigo en Vista para el Login
"""
#from rest_framework.views import APIView
#from .models import Registros
# from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Respuestaschatbot
from .models import Registros
from .models import RegistroInicioSesion
from .models import RegistroCierreSesion
# Create your views here.
# @login_required(login_url='login')



def grafica(request):
    registros = Respuestaschatbot.objects.all()
    return {'registros': registros}

def tuvista1(request):
    # Realiza una consulta que cuente las filas con 'SI' en la columna pregunta1
    count = Respuestaschatbot.objects.filter(pregunta1="Si").count()
    return {'count_si': count}

def tuvista2(request):
    # Realiza una consulta que cuente las filas con 'NO' en la columna pregunta1
    count2 = Respuestaschatbot.objects.filter(pregunta1="No").count()
    return {'count_no': count2}

def HomePage(request):
    grafica_data = grafica(request)
    tuvista_data = tuvista1(request)
    tuvista_data2 = tuvista2(request)
    
    # Combina los contextos de ambas vistas en un solo diccionario
    context = {**grafica_data, **tuvista_data, **tuvista_data2}
    
    return render(request, 'home.html', context)













# from .models import Respuestaschatbot

# def grafica(request):
#     registros = Respuestaschatbot.objects.all()
#     return {'registros': registros}

# def tuvista(request):
#     consulta1 = Respuestaschatbot.objects.all()
#     count = consulta1.count()
#     return {'registros': consulta1, 'count': count}

# def HomePage(request):
#     grafica_data = grafica(request)
#     tuvista_data = tuvista(request)
    
#     # Combina los contextos de ambas vistas en un solo diccionario
#     context = {**grafica_data, **tuvista_data}
    
#     return render(request, 'home.html', context)

















# from .models import Respuestaschatbot


# def grafica(request):
#     # Recupera los registros de la tabla Respuestaschatbot
#     registros = Respuestaschatbot.objects.all()

#     # Ahora tienes la variable 'registros' que contiene todos los datos de la tabla
#     return render(request, 'home.html', {'registros': registros})

# def tuvista(request):
#     registros2 = Respuestaschatbot.objects.all()  # Reemplaza 'TusRegistros' con el nombre de tu modelo de registros
#     count = registros2.count()
#     return render(request, 'home.html', {'registros': registros2, 'count': count})


# def HomePage(request):
#     """a"""
#     return tuvista(request), grafica(request)

    # return render (request, 'home.html')



def SignupPage(request):
    """b"""
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        # Validar si el usuario ya existe
        if Registros.objects.filter(uname=uname).exists():  #Validar si el usuario ya existe
            messages.error(request, "Usuario duplicado")
            return render (request,'registro.html')

        # Validar si el correo electrónico ya existe
        if Registros.objects.filter(email=email).exists():
            messages.error(request, "Correo electrónico duplicado")
            return render(request, 'registro.html')
        
        if pass1!=pass2:
            messages.error(request, "La Contraseña no coincide")
            return render (request,'registro.html')
        else:
            my_user=Registros(uname=uname,email=email,pass1=pass1,pass2=pass2)
            my_user.save()
            contact(request)
            return redirect('login')

    return render (request,'registro.html')


def LoginPage(request):
    """c"""
    # if request.method=='POST':
    #     username=request.POST.get('username')
    #     pass1=request.POST.get('pass')
    #     # print(username,pass1)
    #     user=authenticate(request,username=username,password=pass1)
    #     if user is not None:
    #         login(request,user)
    #         messages.success(request, "Usuario registrado exitosamente")
    #         return redirect('home')
    #     else:
    #         messages.error(request, "El Usuario o Contraseña son Incorrectos")
    if request.method == 'POST':
        uname = request.POST['username']
        pass1 = request.POST['pass']
        # Busca un usuario
        try:
            usuario = Registros.objects.get(uname=uname)
        except Registros.DoesNotExist:
            usuario = None

        if usuario is not None and usuario.pass1 == pass1:
            # autentica al usuario
            request.session['username'] = uname  # Almacena el ID del usuario en la sesión
            
            # Registra el inicio de sesión en la nueva tabla
            registro_inicio_sesion = RegistroInicioSesion(usuario=usuario)
            registro_inicio_sesion.save()
            
            return redirect("home")  # ir a la página de inicio
        else:
            # Si las credenciales no son válidas, muestra un mensaje de error
            messages.error(request, 'El Usuario o Contraseña son Incorrectos')

    return render (request, 'login.html')


def LogoutPage(request):
    # logout(request)
    # Registra el cierre de sesión al obtener el usuario actual
    if 'username' in request.session:
        usuario_actual = Registros.objects.get(uname=request.session['username'])
        registro_cierre_sesion = RegistroCierreSesion(usuario=usuario_actual)
        registro_cierre_sesion.save()

    logout(request)
    
    return redirect('login')

def calendario_view(request):
    return render(request, 'calendario.html')

def contact(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        #subject=request.POST['subject']
        #message=request.POST['message']

        template = render_to_string('email_template.html', {
            'name': username,
            'email': email,
            #'message': message
        })

        email = EmailMessage(
            subject='Confirmacion de registro',
            body=template,
            from_email=settings.EMAIL_HOST_USER,
            to=[email]
         )

        email.fail_silenty = False
        email.send()
        messages.success(request, "Registro exitoso se ha enviado un mensaje a tu correo")
        return redirect('login')
