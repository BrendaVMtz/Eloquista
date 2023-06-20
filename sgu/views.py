from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import TeacherSignUpForm, ParentSignUpForm
from .models import initUser, Teacher, Parent


# Create your views here.


#array vacio

#si array == vacio
# vistas restringidqas
#array == lleno 
# vista de usuario

def teacher_signup(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            teacher = Teacher.objects.create(user=user)
            # Additional processing or redirection
            return redirect('login')
    else:
        form = TeacherSignUpForm()
    return render(request, 'signup.html', {'form': form})

def parent_signup(request):
    if request.method == 'POST':
        form = ParentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            parent = Parent.objects.create(user=user)
            # Additional processing or redirection
            return redirect('login')
    else:
        form = ParentSignUpForm()
    return render(request, 'signup.html', {'form': form})
#redirecciona

def seleccionPerfil(request):
        return render(request, 'sel_perfil.html')

def login(request):
        return render(request, 'login.html')
#llenar array

def profile(request,username):
        #username = get_object_or_404(usuario,nombreDeUsuario=username)
        return HttpResponse("<h2>Hola %s</h2>" % username.nombreDeUsuario)
#solo con vista restringida 
