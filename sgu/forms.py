from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import padre,profesor,salud

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(help_text='Ingresa un correo.')

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2','first_name','last_name']


class ParentSignUpForm(forms.ModelForm):
    class Meta:
        model = padre
        fields = ('calle', 'numero', 
                  'delegacion', 'codigo_postal',
                  'numero_de_telefono')

class TeacherSignUpForm(forms.ModelForm):
    class Meta:
        model = profesor
        fields = ('institucion', 'titulo_academico', 
                  'delegacion', 'numero_de_telefono')

class DoctorSignUpForm(forms.ModelForm):
    class Meta:
        model = salud
        fields = ('institucion', 'cedula', 
                  'delegacion', 'numero_de_telefono')

