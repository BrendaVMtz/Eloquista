from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h2>Bienvenido</h2>")

def acerca(request):
    return HttpResponse("<h2>Somos una aplicacion</h2>")

def contacto(request):
    return HttpResponse("<h2>Contactanos</h2>")
