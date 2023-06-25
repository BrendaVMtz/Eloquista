from django.contrib import admin
from .models import usuario,Tarea,Profesor, Padre, Salud, Alumno

# Register your models here.

admin.site.register(usuario)
admin.site.register(Tarea)
admin.site.register(Profesor)
admin.site.register(Padre)
admin.site.register(Salud)
admin.site.register(Alumno)