from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import initUser, Teacher, Parent

class TeacherSignUpForm(UserCreationForm):
    # Add fields specific to teacher signup form

    class Meta:
        model = initUser
        fields = ('username', 'password1', 'password2')

class ParentSignUpForm(UserCreationForm):
    # Add fields specific to parent signup form

    class Meta:
        model = initUser
        fields = ('username', 'password1', 'password2')

class RegistroUsuarioForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    username = forms.CharField(label='Nombre de usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    correo = forms.CharField(label='Correo', widget=forms.EmailInput)

class registroPadre(forms.Form):
    calle = forms.CharField(label='Nombre', max_length=100)
    numero = forms.CharField(label='Apellido', max_length=100)
    delegacion = forms.CharField(label='Nombre de usuario', max_length=100)
    telefono = forms.CharField(label='Contraseña', widget=forms.NumberInput)

class registroProfesor(forms.Form):
    cedula = forms.CharField(label='Nombre', max_length=100)
    institucion = forms.CharField(label='Apellido', max_length=100)
    delegacion = forms.CharField(label='Nombre de usuario', max_length=100)
    telefono = forms.CharField(label='Contraseña', widget=forms.NumberInput)

