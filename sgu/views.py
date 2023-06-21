from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from verify_email.email_handler import send_verification_email

#from .models import padre
# from .forms import ParentSignUpForm,TeacherSignUpForm,DoctorSignUpForm

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], 
                    password=request.POST["password1"])
                user.save()
                #inactive_user = send_verification_email(request, form)
                login(request, user)
                return redirect('/home')
            except IntegrityError:
                return render(request, 'registro.html', {"form": UserCreationForm, "error": "Usuario ya existe."})

        return render(request, 'registro.html', {"form": UserCreationForm, "error": "Contraseñas no coinciden."})

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'iniciar_sesion.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciar_sesion.html', {"form": AuthenticationForm, "error": "Nombre de usuario o contraseña incorrectos."})

        login(request, user)
        return redirect('home')

def home(request):
    return render(request, 'home.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('/')

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