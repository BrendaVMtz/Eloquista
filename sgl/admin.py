from django.contrib import admin
from .models import Leccion,Ejercicio,progresoEjercicios,progresoLecciones

# Register your models here.

# Register your models here.
admin.site.register(Leccion)
admin.site.register(Ejercicio)
admin.site.register(progresoLecciones)
admin.site.register(progresoEjercicios)