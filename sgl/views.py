from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def home(request):
        return HttpResponse("<h2>Selecciona tu perfil</h2>")

def leccion(request):
        return HttpResponse("<h2>Registrarse</h2>")
