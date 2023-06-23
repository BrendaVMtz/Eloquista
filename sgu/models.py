from django.contrib.auth.models import AbstractUser
from django.db import models

class usuario(AbstractUser):
    numero_de_telefono = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Tarea(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Profesor(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    institucion = models.CharField(max_length=100)
    titulo_academico = models.CharField(max_length=100)

    def __str__(self):
        return 'Profesor: ' + self.usuario.username

class Alumno(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre


# class padre(models.Model):
#     usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
#     calle = models.CharField(max_length=100)
#     numero = models.CharField(max_length=100)
#     delegacion = models.CharField(max_length=100)
#     codigo_postal = models.CharField(max_length=100)
#     numero_de_telefono = models.CharField(max_length=100)
    
#     def __str__(self):
#         return 'Padre: ' + self.usuario.username

# class profesor(models.Model):
#     usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
#     institucion = models.CharField(max_length=100)
#     titulo_academico = models.CharField(max_length=100)
#     delegacion = models.CharField(max_length=100)
#     numero_de_telefono = models.CharField(max_length=100)

#     def __str__(self):
#         return 'Profesor: ' + self.usuario.username

# class salud(models.Model):
#     usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
#     institucion = models.CharField(max_length=100)
#     cedula = models.CharField(max_length=100)
#     delegacion = models.CharField(max_length=100)
#     numero_de_telefono = models.CharField(max_length=100)

#     def __str__(self):
#         return 'Profesional-salud: ' + self.usuario.username

     