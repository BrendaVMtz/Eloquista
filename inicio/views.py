from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def acerca(request):
    return HttpResponse("<h2>Somos una aplicacion</h2>")

def contacto(request):
    return HttpResponse("<h2>Contactanos</h2>")
