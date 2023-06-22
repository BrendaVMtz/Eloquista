from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect("/home")
    else:
        return render(request, 'index.html')

def acerca(request):
    if request.user.is_authenticated:
        return redirect("/home")
    else:
        return render(request, 'acerca.html')

def contacto(request):
    if request.user.is_authenticated:
        return redirect("/home")
    else:
        return render(request, 'contacto.html')
