from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.TextField(max_length=20, blank=False)
    is_verified = models.BooleanField(default=False)

# class padre(models.Model):
#     #usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#     calle = models.CharField(max_length=100)
#     numero = models.CharField(max_length=100)
#     delegacion = models.CharField(max_length=100)
#     codigo_postal = models.CharField(max_length=100)
#     numero_de_telefono = models.CharField(max_length=100)
    
#     def __str__(self):
#         return 'Padre: ' #+ self.usuario.username

# class profesor(models.Model):
#     #usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#     institucion = models.CharField(max_length=100)
#     titulo_academico = models.CharField(max_length=100)
#     delegacion = models.CharField(max_length=100)
#     numero_de_telefono = models.CharField(max_length=100)

#     def __str__(self):
#         return 'Profesor: ' #+ self.usuario.username

# class salud(models.Model):
#     #usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#     institucion = models.CharField(max_length=100)
#     cedula = models.CharField(max_length=100)
#     delegacion = models.CharField(max_length=100)
#     numero_de_telefono = models.CharField(max_length=100)

#     def __str__(self):
#         return 'Profesional-salud: ' #+ self.usuario.username

     