from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Tarea,usuario, Profesor,Alumno
from django.utils.translation import gettext_lazy as _  # Agrega esta línea

class RegistroForm(UserCreationForm):
    # Cambia los nombres de los campos
    username = forms.CharField(label=_("Nombre de usuario"))
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

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['institucion', 'titulo_academico','delegacion']

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'edad']

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField(help_text='Ingresa un correo.')

#     class Meta:
#         model = usuario
#         fields = ['username', 'password1', 'password2','first_name','last_name']

# class TareaForm(forms.ModelForm):
#     class Meta:
#         model = Tarea
#         fields = ('nombre', 'descripcion')

# class ParentSignUpForm(forms.ModelForm):
#     class Meta:
#         model = padre
#         fields = ('calle', 'numero', 
#                   'delegacion', 'codigo_postal',
#                   'numero_de_telefono')

# class TeacherSignUpForm(forms.ModelForm):
#     class Meta:
#         model = profesor
#         fields = ('institucion', 'titulo_academico', 
#                   'delegacion', 'numero_de_telefono')

# class DoctorSignUpForm(forms.ModelForm):
#     class Meta:
#         model = salud
#         fields = ('institucion', 'cedula', 
#                   'delegacion', 'numero_de_telefono')

