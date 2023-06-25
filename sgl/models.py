from django.db import models
from sgu.models import usuario

class Leccion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class Pregunta(models.Model):
    examen = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    pregunta = models.TextField()
    
    def __str__(self):
        return self.pregunta

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion = models.TextField()
    es_correcta = models.BooleanField()

    def __str__(self):
        return self.pregunta.pregunta + self.opcion

class RespuestaUsuario(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} - {self.pregunta.pregunta}"

class Calificacion(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    examen = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.calificacion}"

# from django.db import models
# from sgu.models import Alumno

# from django.db.models.signals import post_save
# from django.dispatch import receiver


# # Create your models here.

# class Leccion(models.Model):
#     titulo = models.CharField
#     numero_de_telefono = models.CharField(max_length=100)


# class Ejercicio(models.Model):
#     leccion = models.ForeignKey(Leccion,on_delete=models.CASCADE)
#     tipo = models.CharField
#     enunciado = models.CharField
#     opcionesRespuesta = models.CharField
#     respuestaCorrecta = models.CharField

# # class progresoEjercicios(models.Model):
# #     #idAlumno=models.ForeignKey(alumno,on_delete=models.CASCADE)
# #     leccion = models.ForeignKey(Leccion,on_delete=models.CASCADE)
# #     ejercicioCompleto = models.BooleanField(default=False)
# #     # class Meta:
# #     #     unique_together = ('idAlumno','idEjercicio')

# class progresoLecciones(models.Model):
#     #idAlumno=models.ForeignKey(alumno,on_delete=models.CASCADE)
#     idLeccion= models.ForeignKey(Leccion,on_delete=models.CASCADE)
#     leccionCompleta = models.BooleanField(default=False)
#     puntuacion = models.IntegerField()
#     # class Meta:
#     #     unique_together = ('idAlumno','idLeccion')

# # @receiver(post_save, sender=progresoEjercicios)
# # def verificar_leccion_completa(sender, instance, **kwargs):
# #     leccion = instance.idEjercicio.idLeccion
# #     alumno = instance.idAlumno

# #     if not Ejercicio.objects.filter(idLeccion=leccion, id__in=progresoEjercicios.objects.filter(idAlumno=alumno, ejercicioCompleto=False)).exists():
# #         progreso = progresoLecciones.objects.get(idAlumno=alumno, idLeccion=leccion)
# #         progreso.leccionCompleta = True
# #         progreso.save()
