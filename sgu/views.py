from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import usuario,cuidador,padre,profesor
from django.shortcuts import get_object_or_404
from .forms import RegistroUsuarioForm, registroPadre, registroProfesor
from django.contrib import messages

# Create your views here.


#array vacio

#si array == vacio
# vistas restringidqas
#array == lleno 
# vista de usuario

def signup(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data['username']
            if usuario.objects.filter(nombreDeUsuario=nombre_usuario).exists():
                messages.error(request, 'El nombre de usuario ya existe. Por favor, elige otro.')
                return redirect('/comenzar/signup/')
            else:
                nuevo_usuario = usuario.objects.create(
                    nombre=form.cleaned_data['nombre'],
                    apellido=form.cleaned_data['apellido'],
                    nombreDeUsuario=form.cleaned_data['username'],
                    contrasena=form.cleaned_data['password']
                )
                #pero todos los usuarios nuevos son cuidadores, luego cuidador se divide en padre o profesor
                cuidador.objects.create(
                    nombreDeUsuario=nuevo_usuario,
                    correoElectronico=form.cleaned_data['correo']
                )
                return render(request, 'signup2.html', {'registration_successful': True}) 
    else:
        form = RegistroUsuarioForm()

    return render(request, 'signup.html', {'form': form}) #un ejemlo pls


#redirecciona

def seleccionPerfil(request):
        return render(request, 'sel_perfil.html')

def login(request):
        return render(request, 'login.html')
#llenar array

def profile(request,username):
        username = get_object_or_404(usuario,nombreDeUsuario=username)
        return HttpResponse("<h2>Hola %s</h2>" % username.nombreDeUsuario)
#solo con vista restringida 
