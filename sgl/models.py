from django.db import models
from sgu.models import alumno

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Leccion(models.Model):
    id = models.IntegerField(primary_key= True)
    nivelRequerido = models.IntegerField
    titulo = models.CharField

class Ejercicio(models.Model):
    idLeccion = models.ForeignKey(Leccion,on_delete=models.CASCADE)
    tipo = models.CharField
    enunciado = models.CharField
    opcionesRespuesta = models.CharField
    respuestaCorrecta = models.CharField

class progresoEjercicios(models.Model):
    idAlumno=models.ForeignKey(alumno,on_delete=models.CASCADE)
    idEjercicio = models.ForeignKey(Ejercicio,on_delete=models.CASCADE)
    ejercicioCompleto = models.BooleanField(default=False)
    class Meta:
        unique_together = ('idAlumno','idEjercicio')

class progresoLecciones(models.Model):
    idAlumno=models.ForeignKey(alumno,on_delete=models.CASCADE)
    idLeccion= models.ForeignKey(Leccion,on_delete=models.CASCADE)
    leccionCompleta = models.BooleanField(default=False)
    class Meta:
        unique_together = ('idAlumno','idLeccion')

@receiver(post_save, sender=progresoEjercicios)
def verificar_leccion_completa(sender, instance, **kwargs):
    leccion = instance.idEjercicio.idLeccion
    alumno = instance.idAlumno

    if not Ejercicio.objects.filter(idLeccion=leccion, id__in=progresoEjercicios.objects.filter(idAlumno=alumno, ejercicioCompleto=False)).exists():
        progreso = progresoLecciones.objects.get(idAlumno=alumno, idLeccion=leccion)
        progreso.leccionCompleta = True
        progreso.save()
