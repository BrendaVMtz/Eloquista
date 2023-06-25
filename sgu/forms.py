from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Tarea,usuario,Alumno, Profesor, Padre, Salud
from django.utils.translation import gettext_lazy as _  # Agrega esta línea

class RegistroForm(UserCreationForm):
    # Cambia los nombres de los campos
    username = forms.CharField(label=_("Nombre de usuario"))
    email = forms.CharField(label=_("Correo electrónico"))
    password1 = forms.CharField(label=_("Contraseña"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Confirmar contraseña"), widget=forms.PasswordInput)

    class Meta:
        model = usuario
        fields = ('username', 'password1', 'password2')  # Agrega otros campos si es necesario

class InicioSesionForm(AuthenticationForm):
    # Cambia los nombres de los campos
    username = forms.CharField(label=_("Nombre de usuario"))
    password = forms.CharField(label=_("Contraseña"), widget=forms.PasswordInput)

    class Meta:
        model = usuario
        fields = ('username', 'password')

class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion']

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'edad','identificacion', 'diagnostico']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['institucion', 'titulo_academico','delegacion']

class ParentForm(forms.ModelForm):
    class Meta:
        model = Padre
        fields = ['calle', 'numero','delegacion','codigo_postal']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Salud
        fields = ['institucion', 'cedula','delegacion']

