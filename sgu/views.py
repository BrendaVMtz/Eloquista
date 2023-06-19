from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import usuario
from django.shortcuts import get_object_or_404

# Create your views here.

def seleccionPerfil(request):
        return HttpResponse("<h2>Selecciona tu perfil</h2>")

def signup(request):
        return HttpResponse("<h2>Registrarse</h2>")

def login(request):
        return HttpResponse("<h2>login</h2>")

def profile(request,username):
        username = get_object_or_404(usuario,nombreDeUsuario=username)
        return HttpResponse("<h2>Hola %s</h2>" % username.nombreDeUsuario)
