from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserRegisterForm

from .models import padre,profesor,salud
from .forms import ParentSignUpForm,TeacherSignUpForm,DoctorSignUpForm

# Create your views here.


def registro(request):
    # Logged in user can't register a new account
    if request.user.is_authenticated:
        return redirect("/home")

    if request.method == 'POST':
        userForm = UserRegisterForm(request.POST)
        if userForm.is_valid():
            user = userForm.save()
            login(request, user)
            return redirect('/sel_perfil')
        else:
            for error in list(userForm.errors.values()):
                print(request, error)

    else:
        userForm = UserRegisterForm()

    return render(
        request = request,
        template_name = "registro.html",
        context={"userForm":userForm}
        )

def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect("/home")

    if request.method == 'GET':
        return render(request, 'iniciar_sesion.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciar_sesion.html', {"form": AuthenticationForm, "error": "Nombre de usuario o contraseña incorrectos."})

        login(request, user)
        return redirect('/home')

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect("/")

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('/')

@login_required
def sel_perfil(request):
    if request.user.is_authenticated:
        return render(request, 'sel_perfil.html')
    else:
        return redirect("/")

@login_required
def registro_padre(request):
    if request.method == "POST":
        parentFrom = ParentSignUpForm(request.POST)
        if parentFrom.is_valid():
            parent_profile = form.save(commit=False)
            parent_profile.usuario = request.user
            print(parent_profile.usuario.username)
            parent_profile.save()
            return redirect('home')
        else:
            return render(request, 'registro_padre.html', {"form": ParentSignUpForm, "name":name, "error": "Error en los datos"})
    else:
        parentFrom = ParentSignUpForm()
    
    name = 'Padres y tutores'
    return render(request, 'registro_padre.html', {"form": ParentSignUpForm, "name":name})
    

 
@login_required
def registro_profesor(request):
    if request.method == "GET":
        name = 'Profesores'
        return render(request, 'registro_padre.html', {"form": TeacherSignUpForm, "name":name})
    else:
        form = TeacherSignUpForm(request.POST)
        try:
             teacher_profile = form.save(commit=False)
             teacher_profile.user = request.user
             teacher_profile.save()
             return redirect('home')
        except ValueError:
            return render(request, 'registro_padre.html', {"form": TeacherSignUpForm, "name":name, "error": "Error en los datos"})

@login_required
def registro_salud(request):
    name = 'Profesionales de la salud'
    return render(request, 'registro_padre.html', {"form": DoctorSignUpForm, "name":name})