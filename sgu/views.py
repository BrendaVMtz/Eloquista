from django.shortcuts import render, redirect
from .forms import TeacherSignUpForm, ParentSignUpForm

def seleccionarPerfil(request):
    return render(request, 'perfil.html')

from django.shortcuts import render, redirect
from .forms import TeacherSignUpForm, ParentSignUpForm, UserSignUpForm
from .models import User, Teacher, Parent

def teacher_signup(request):
    if request.method == 'POST':
        userForm = UserSignUpForm(request.POST)
        form = TeacherSignUpForm(request.POST)
        if userForm.is_valid() and form.is_valid():
            user = userForm.save(commit=False)
            user.is_teacher = True
            user.save()
            teacher = form.save(commit=False)
            teacher.user = user
            teacher.save()
            return redirect('home')  # Replace 'home' with the appropriate URL
    else:
        userForm = UserSignUpForm()
        form = TeacherSignUpForm()
    return render(request, 'signup.html', {'userForm': userForm, 'form': form})

def parent_signup(request):
    if request.method == 'POST':
        form = ParentSignUpForm(request.POST)
        if form.is_valid():
            parent = form.save(commit=False)
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create(username=username, email=email, password=password, is_parent=True)
            parent.user = user
            parent.save()
            return redirect('home')  # Replace 'home' with the appropriate URL
    else:
        form = ParentSignUpForm()
    return render(request, 'signup.html', {'form': form})
