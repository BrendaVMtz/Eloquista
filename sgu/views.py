from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def seleccionPerfil(request):
        return HttpResponse("<h2>Selecciona tu perfil</h2>")

def signup(request):
        return HttpResponse("<h2>Registrarse</h2>")

def login(request):
        return HttpResponse("<h2>login</h2>")
