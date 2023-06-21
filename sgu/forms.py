from django import forms
from .models import padre,profesor,salud

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

