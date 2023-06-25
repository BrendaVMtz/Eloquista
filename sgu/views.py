from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Tarea, usuario, Alumno, Profesor, Padre, Salud
from django.shortcuts import render, redirect
from .forms import RegistroForm, TareaForm, AlumnoForm, ProfesorForm, ParentForm, DoctorForm

# Create your views here.


def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password, email=email)
            login(request, user)
            return redirect('sel_perfil')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

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
def agregar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user
            tarea.save()
            return redirect('agregar_tarea')
    else:
        form = TareaForm()
    tareas = Tarea.objects.filter(usuario=request.user)  # Agrega esta línea
    return render(request, 'home.html', {'form': form, 'tareas': tareas})  # Agrega 'tareas' en el contexto


@login_required
def registro_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST, request.FILES)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.usuario = request.user
            alumno.identificacion = request.FILES['identificacion']
            alumno.diagnostico = request.FILES['diagnostico']
            alumno.save()
            return redirect('home')
    else:
        form = AlumnoForm()
    alumnos = Alumno.objects.filter(usuario=request.user)  
    return render(request, 'registro_alumno.html', {'form': form, 'alumnos': alumnos}) 

@login_required
def registro_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = form.save(commit=False)
            profesor.usuario = request.user
            profesor.save()
            return redirect('registro_alumno')
    else:
        form = ProfesorForm()
    profesores = Profesor.objects.filter(usuario=request.user)  
    return render(request, 'registro_profesor.html', {'form': form, 'profesores': profesores})  # Agrega 'tareas' en el contexto

@login_required
def registro_padre(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            padre = form.save(commit=False)
            padre.usuario = request.user
            padre.save()
            return redirect('registro_alumno')
    else:
        form = ParentForm()
    padres = Padre.objects.filter(usuario=request.user)  
    return render(request, 'registro_padre.html', {'form': form, 'padres': padres})  

@login_required
def registro_salud(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.usuario = request.user
            doctor.save()
            return redirect('registro_alumno')
    else:
        form = DoctorForm()
    doctores = Salud.objects.filter(usuario=request.user)  
    return render(request, 'registro_salud.html', {'form': form, 'doctores': doctores})  



# def registro(request):
#     # Logged in user can't register a new account
#     if request.user.is_authenticated:
#         return redirect("/home")

#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('/sel_perfil')
#         else:
#             for error in list(form.errors.values()):
#                 print(request, error)

#     else:
#         form = UserRegisterForm()

#     return render(
#         request = request,
#         template_name = "registro.html",
#         context = {"userForm":form}
#         )

# def iniciar_sesion(request):
#     if request.user.is_authenticated:
#         return redirect("/home")

#     if request.method == 'GET':
#         return render(request, 'iniciar_sesion.html', {"form": AuthenticationForm})
#     else:
#         user = authenticate(
#             request, username=request.POST['username'], password=request.POST['password'])
#         if user is None:
#             return render(request, 'iniciar_sesion.html', {"form": AuthenticationForm, "error": "Nombre de usuario o contraseña incorrectos."})

#         login(request, user)
#         return redirect('/home')

# def home(request):
#     if request.user.is_authenticated:
#         return render(request, 'home.html')
#     else:
#         return redirect("/")

# @login_required
# def cerrar_sesion(request):
#     logout(request)
#     return redirect('/')

# @login_required
# def sel_perfil(request):
#     if request.user.is_authenticated:
#         return render(request, 'sel_perfil.html')
#     else:
#         return redirect("/")

# def agregar_tarea(request):
#     if request.method == 'POST':
#         form = TareaForm(request.POST)
#         if form.is_valid():
#             tarea = form.save(commit=False)
#             tarea.usuario = request.user
#             tarea.save()
#             return redirect('home')
#     else:
#         form = TareaForm()
#     return render(request, 'home.html', {'form': form})

# def mostrar_tareas(request):
#     tareas = Tarea.objects.filter(usuario=request.user)
#     return render(request, 'home.html', {'tareas': tareas})

# @login_required
# def registro_padre(request):
#     if request.method == "GET":
#         return render(request, 'registro_padre.html', {"form": ParentSignUpForm})
#     else:
#         try:
#             form = ParentSignUpForm(request.POST)
#             new_task = form.save(commit=False)
#             new_task.usuario = request.user
#             new_task.save()
#             return redirect('home')
#         except ValueError:
#             return render(request, 'registro_padre.html', {"form": ParentSignUpForm, "error": "Error creating task."})



 
# @login_required
# def registro_profesor(request):
#     if request.method == "GET":
#         name = 'Profesores'
#         return render(request, 'registro_padre.html', {"form": TeacherSignUpForm, "name":name})
#     else:
#         form = TeacherSignUpForm(request.POST)
#         try:
#              teacher_profile = form.save(commit=False)
#              teacher_profile.user = request.user
#              teacher_profile.save()
#              return redirect('home')
#         except ValueError:
#             return render(request, 'registro_padre.html', {"form": TeacherSignUpForm, "name":name, "error": "Error en los datos"})

# @login_required
# def registro_salud(request):
#     name = 'Profesionales de la salud'
#     return render(request, 'registro_padre.html', {"form": DoctorSignUpForm, "name":name})