from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nombreDeUsuario = models.CharField(max_length=50, unique=True,primary_key=True)
    contrasena = models.CharField(max_length=50)


class cuidador(models.Model):
    nombreDeUsuario = models.OneToOneField(usuario,on_delete=models.CASCADE)
    correoElectronico = models.CharField(max_length=100)

class padre(cuidador):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)    
    delegacion = models.CharField(max_length=100)    
    telefono = models.PositiveIntegerField  

class salud(cuidador):
    cedula = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)    
    delegacion = models.CharField(max_length=100)    
    telefono = models.PositiveIntegerField  

class profesor(cuidador):
    cedula = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)    
    delegacion = models.CharField(max_length=100)    
    telefono = models.PositiveIntegerField    

class alumno(models.Model):
    #idCuidador = models.ForeignKey(cuidador,on_delete=models.CASCADE, related_name='idCuidador')
    nombreDeUsuario = models.OneToOneField(usuario,on_delete=models.CASCADE)
    edad = models.IntegerField(
    validators=[
        MinValueValidator(0, message='El valor debe ser igual o mayor a 0.'),
        MaxValueValidator(150, message='El valor debe ser igual o menor a 150.')
    ]
)

class alumno_cuidador(models.Model):
    alumno = models.ForeignKey(alumno,on_delete=models.SET_NULL,null=True)
    cuidador = models.ForeignKey(cuidador,on_delete=models.CASCADE)