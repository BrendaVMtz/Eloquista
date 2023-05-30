from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h2>Bienvenido</h2>")

def about(request):
    return HttpResponse("<h2>Somos una aplicacion</h2>")
