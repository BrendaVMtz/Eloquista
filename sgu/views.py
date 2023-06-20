from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import usuario,cuidador
from django.shortcuts import get_object_or_404
from .forms import registroUsuario
from django.contrib import messages

# Create your views here.


#array vacio

#si array == vacio
# vistas restringidqas
#array == lleno 
# vista de usuario

def signup(request):
        if request.method == 'POST':
                nombre_usuario = request.POST['username']
                print(nombre_usuario)
                if usuario.objects.filter(nombreDeUsuario = nombre_usuario).exists():
                        messages.error(request, 'Nombre de usuario ya existe')
                        return redirect('/comenzar/signup/')
                else:
                        nuevo_usuario = usuario.objects.create(
                                nombre = request.POST['nombre'],
                                apellido = request.POST['apellido'],
                                nombreDeUsuario = request.POST['username'],
                                contrasena = request.POST['password']
                        )
                        cuidador.objects.create(
                                nombreDeUsuario =nuevo_usuario,
                                correoElectronico = request.POST['correo']
                        )
                        return redirect('/comenzar/sel_perfil/')        
        else:
                return render(request, 'signup.html',{
                        'form':registroUsuario
                })
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
