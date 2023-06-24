from django.contrib import admin
from .models import Examen, Pregunta, Opcion, RespuestaUsuario, Calificacion
# from .models import Leccion,Ejercicio,progresoEjercicios,progresoLecciones

# Register your models here.

# Register your models here.
admin.site.register(Examen)
admin.site.register(Pregunta)
admin.site.register(Opcion)
admin.site.register(RespuestaUsuario)
admin.site.register(Calificacion)
# admin.site.register(progresoLecciones)
# admin.site.register(progresoEjercicios)