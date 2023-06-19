from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class cuidador(models.Model):
    nombreDeUsuario = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correoElectronico = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=50)

class alumno(models.Model):
    idCuidador = models.ForeignKey(cuidador,on_delete=models.CASCADE, default=0)
    nombreDeUsuario = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    edad = models.IntegerField(
    validators=[
        MinValueValidator(0, message='El valor debe ser igual o mayor a 0.'),
        MaxValueValidator(150, message='El valor debe ser igual o menor a 150.')
    ]
)