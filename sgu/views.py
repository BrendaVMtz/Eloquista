from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import usuario
from django.shortcuts import get_object_or_404
from .forms import registroUsuario

# Create your views here.


#array vacio

#si array == vacio
# vistas restringidqas
#array == lleno 
# vista de usuario

def signup(request):
        if request.method == 'GET':
                return render(request, 'signup.html',{
                        'form':registroUsuario
                })
        else:
                print(request.POST['nombre'])
                return redirect('/comenzar/sel_perfil/')
#redirecciona

def seleccionPerfil(request):
        return HttpResponse("<h2>Selecciona tu perfil</h2>")

def login(request):
        return render(request, 'login.html')
#llenar array

def profile(request,username):
        username = get_object_or_404(usuario,nombreDeUsuario=username)
        return HttpResponse("<h2>Hola %s</h2>" % username.nombreDeUsuario)
#solo con vista restringida 
