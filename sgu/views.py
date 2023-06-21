from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], 
                    password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('/sel_perfil')
            except IntegrityError:
                return render(request, 'registro.html', {"form": UserCreationForm, "error": "Usuario ya existe."})

        return render(request, 'registro.html', {"form": UserCreationForm, "error": "Contraseñas no coinciden."})

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'iniciar_sesion.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciar_sesion.html', {"form": AuthenticationForm, "error": "Nombre de usuario o contraseña incorrectos."})

        login(request, user)
        return redirect('home')

def sel_perfil(request):
     return render(request, 'sel_perfil.html')

def home(request):
    return render(request, 'home.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('/')