from django import forms

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

