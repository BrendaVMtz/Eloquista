from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserRegisterForm
# Create your views here.

# def home(request):
#     return render(request, 'home.html')

def registro(request):
    # Logged in user can't register a new account
    if request.user.is_authenticated:
        return redirect("/home")

    if request.method == 'POST':
        userForm = UserRegisterForm(request.POST)
        if userForm.is_valid():
            user = userForm.save()
            login(request, user)
            return redirect('/home')
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
    return render(request, 'home.html')

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('/')




#from .models import padre
# from .forms import ParentSignUpForm,TeacherSignUpForm,DoctorSignUpForm

# def iniciar_sesion(request):
#     if request.method == 'GET':
#         return render(request, 'iniciar_sesion.html', {"form": AuthenticationForm})
#     else:
#         user = authenticate(
#             request, username=request.POST['username'], password=request.POST['password'])
#         if user is None:
#             return render(request, 'iniciar_sesion.html', {"form": AuthenticationForm, "error": "Nombre de usuario o contraseña incorrectos."})

#         login(request, user)
#         return redirect('home')

# def cerrar_sesion(request):
#     logout(request)
#     return redirect('/')

# def sel_perfil(request):
#      return render(request, 'sel_perfil.html')

# def registro_padre(request):
#      if request.method == "GET":
#         name = 'Padres y tutores'
#         return render(request, 'registro_padre.html', {"form": ParentSignUpForm, "name":name})
#      else:
#         form = ParentSignUpForm(request.POST)
#         try:
#              parent_profile = form.save(commit=False)
#              #parent_profile.user = request.user
#              parent_profile.save()
#              return redirect('/home')
#         except ValueError:
#             return render(request, 'registro_padre.html', {"form": ParentSignUpForm, "name":name, "error": "Error en los datos"})


# def registro_profesor(request):
#     name = 'Profesores'
#     return render(request, 'registro_padre.html', {"form": TeacherSignUpForm, "name":name})

# def registro_salud(request):
#     name = 'Profesionales de la salud'
#     return render(request, 'registro_padre.html', {"form": DoctorSignUpForm, "name":name})